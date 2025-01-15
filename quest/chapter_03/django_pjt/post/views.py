from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import F
from .models import Post

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

# 게시글 상세 화면 조회
@login_required    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # 조회 수 증가
    Post.objects.filter(pk=pk).update(views=F('views') + 1)
    
    context = {
        "post": post
    }
    return render(request, "post/post_detail.html", context)

# - 게시글 삭제 처리
@login_required
@require_POST
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("post:post_list")
