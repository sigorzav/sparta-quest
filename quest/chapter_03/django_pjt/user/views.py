from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from .forms import UserCreationForm, UserProfileForm
from .models import User

# ###################################################################################
# MTV & DEF
# ###################################################################################

# 로그인 화면 조회 및 처리
@require_http_methods(["GET", "POST"])
def login(request):
    # 세션이 있는 경우, 게시글 목록 화면 이동
    if request.user.is_authenticated:
        return redirect("post:post_list")
    
    # POST :: 로그인 처리
    #  > 인증 성공 시, 게시글 목록 화면 이동
    #  > 인증 실패 시, 로그인 화면 이동
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        # 인증 성공
        if form.is_valid():
            auth_login(request, form.get_user())
            next = request.GET.get('next')
            print
            next_url = request.GET.get('next', 'post:post_list')
            return redirect(next_url)
        # 인증 실패
        else:
            context = {
                "form": form,
                "error": "Invalid username or password. Please try again."
            }
            return render(request, "user/login.html", context)
    # GET :: 로그인 화면 이동
    else:
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, "user/login.html", context)
    
# 접속 세션 사용자 로그아웃 처리 
@require_POST
def logout(request):
    # 인증된(세션이 존재하는) 경우에만 로그아웃 처리
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("user:login")

# 사용자 회원가입
@require_http_methods(["GET", "POST"])
def signup(request):
    # POST :: 회원가입 처리
    #  > 가입 성공 시, 게시글 목록 화면 이동
    #  > 가입 실패 시, 로그인 화면 이동
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
        else:
            return render(request, "user/signup.html", { "form": form })
    # GET :: 로그인 화면 이동
    else:
        form = UserCreationForm()
        context = {
            "form": form
        }
        return render(request, "user/signup.html", context)
    
# 사용자 프로필 조회 및 작성
@login_required
@require_http_methods(["GET", "POST"])
def user_profile(request):
    user = get_object_or_404(User, pk=request.user.pk)
    
    # POST :: 프로필 저장
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user:user_profile")
    # GET :: 프로필 조회/작성 화면 이동    
    else:
        form = UserProfileForm(instance=user)
        context = {
            "form": form,
            "user": user,
        }
        return render(request, "user/profile.html", context)

