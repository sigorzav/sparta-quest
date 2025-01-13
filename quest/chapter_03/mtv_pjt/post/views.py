from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import PostForm

# [게시글 목록]
# - 게시글 목록 조회
@login_required
def post_list(request):
    return render(request, "post/post_list.html")

# [게시글 작성]
# - 게시글 작성 화면 조회 및 저장
@login_required
@require_http_methods(["GET", "POST"])
def post_create(request):
    # POST :: 로그인 처리
    #  > 인증 성공 시, 게시글 목록 화면 이동
    #  > 인증 실패 시, 로그인 화면 이동
    if request.method == "POST":
        pass
    # GET :: 게시글 작성 화면 이동    
    else:
        form = PostForm()
        context = {
            "form": form
        }
        return render(request, "post/post_create.html", context)        
