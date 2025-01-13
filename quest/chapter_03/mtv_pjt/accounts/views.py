from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm,
)

@require_http_methods(["GET", "POST"])
def login(request):
    # POST 요청인 경우, 로그인 처리
    # 성공 :: 게시물 목록 화면으로
    # 실패 :: 로그인 화면
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("blog:blog_list")
    # GET 요청인 경우, 로그인 화면으로 이동
    else:
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, "accounts/login.html", context)    

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("accounts:login")