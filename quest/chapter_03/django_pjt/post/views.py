from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework import status
from django.db.models import F
from .models import Post, Comment
from .forms import PostForm
from .serializers import CommentSerializers
from django.http import JsonResponse

# ###################################################################################
# MTV & DEF
# ###################################################################################

# 게시글 목록 조회
@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-pk')
    
    # 페이징
    paginator = Paginator(posts, 10)            # 페이지에서 보여줄 포스트 수
    page_number = request.GET.get("page", '1')  # 조회 페이지 번호
    page_obj = paginator.get_page(page_number)  # 해당 페이지 포스트
    
    context = {
        "page_obj": page_obj
    }
    return render(request, "post/post_list.html", context)

# 게시글 작성 화면 조회 및 저장
@login_required
@require_http_methods(["GET", "POST"])
def post_create(request):
    # POST :: 게시글 저장
    #  > 저장 성공 시, 게시글 상세 화면 이동
    #  > 저장 실패 시, 게시글 작성 화면 이동
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post:post_detail", post.pk)
    # GET :: 게시글 작성 화면 이동    
    else:
        form = PostForm()
        context = {
            "form": form,
            "is_update": False,
        }
        return render(request, "post/post_form.html", context)
    
# 게시글 상세 화면 조회
@login_required    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # 조회 수 증가
    Post.objects.filter(pk=pk).update(views=F('views') + 1)
    
    # 좋아요
    if post.likes.filter(id=request.user.id).exists():
        liked = True
    else:
        liked = False
    
    context = {
        "post": post,
        "liked": liked,
        "likes_count": post.get_likes_count        
    }
    return render(request, "post/post_detail.html", context)

# 게시글 수정 화면 조회 및 저장
@login_required
@require_http_methods(["GET", "POST"])
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # POST :: 게시글 수정
    #  > 수정 성공 시, 게시글 상세 화면 이동
    #  > 수정 실패 시, 게시글 작성 화면 이동
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post:post_detail", post.pk)
    # GET :: 게시글 작성 화면 이동    
    else:
        form = PostForm(instance=post)
        context = {
            "form": form,
            "post": post,
            "is_update": True,
        }
        return render(request, "post/post_form.html", context)
    
# 게시글 삭제 처리
@login_required
@require_POST
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("post:post_list")

@login_required
@require_POST
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    serializer = CommentSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        comment = serializer.save(author=request.user, post=post)
        rendered_comment = render(request, 'post/comments.html', {'comment': comment}).content.decode('utf-8')
        
        return JsonResponse({'comment_html': rendered_comment})

# ###################################################################################
# DRF & CLASS
# ###################################################################################

# 공통 APIView
class BaseApiView(APIView):
    
    def get_object(self, model, pk):
        return get_object_or_404(model, pk=pk)

# 좋아요
class LikesAPIView(BaseApiView):
    
    def post(self, request, *args, **kwargs):
        post_pk = self.kwargs.get('post_pk')
        post = self.get_object(Post, post_pk)
        
        # 좋아요 취소
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        # 좋아요 추가
        else:
            post.likes.add(request.user)
            liked = True
        
        data = {
            "liked": liked,
            "likes_count": post.get_likes_count
        }
        return Response(data)
        
# 댓글 조회/작성
class CommentListAPIView(BaseApiView):

    # 댓글 조회
    def get(self, request, *args, **kwargs):
        post_pk = self.kwargs.get('post_pk')
        post = self.get_object(Post, post_pk)
        
        comments = post.comments.all()
        
        serializer = CommentSerializers(comments, many=True)
        return Response(serializer.data)
        
    # 댓글 작성
    def post(self, request, *args, **kwargs):
        post_pk = self.kwargs.get('post_pk')
        post = self.get_object(Post, post_pk)

        serializer = CommentSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 댓글 수정/삭제  
class CommentDetailAPIView(BaseApiView):

    # 댓글 삭제
    def delete(self, request, *args, **kwargs):
        comment_pk = self.kwargs.get('comment_pk')
        comment = self.get_object(Comment, comment_pk)
        comment.delete()
        
        data = {
            "comment_pk": comment_pk,
            "author": comment.author.id,
            "post": comment.post.id,
            "content": comment.content,
        }
        return Response(data)