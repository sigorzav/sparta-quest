from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import PostForm
from .models import Post

# 게시글 목록 조회
@login_required
def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
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
    context = {
        "post": post
    }
    return render(request, "post/post_detail.html", context)

# - 게시글 수정 화면 조회 및 저장
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

# - 게시글 삭제 처리
@login_required
@require_POST
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("post:post_list")
    