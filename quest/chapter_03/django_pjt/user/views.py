from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
# from .forms import UserCreationForm

# 로그인 화면 조회 및 처리
@require_http_methods(["GET", "POST"])
def login(request):
    # POST :: 로그인 처리
    #  > 인증 성공 시, 게시글 목록 화면 이동
    #  > 인증 실패 시, 로그인 화면 이동
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("post:post_list")
    # GET :: 로그인 화면 이동
    else:
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, "user/login.html", context)
    
# - 접속 세션 사용자 로그아웃 처리 
@require_POST
def logout(request):
    # 인증된(세션이 존재하는) 경우에만 로그아웃 처리
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("user:login")    