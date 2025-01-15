from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
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
