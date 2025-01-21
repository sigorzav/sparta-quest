from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import F
from .models import Post
from .forms import PostForm


# 게시글 목록 조회
@login_required
def post_list(request):
    posts = Post.objects.annotate(comments_count=Count('comments')).order_by('-pk')
    
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