from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

# 게시글 목록 조회
@login_required
def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "post/post_list.html", context)
