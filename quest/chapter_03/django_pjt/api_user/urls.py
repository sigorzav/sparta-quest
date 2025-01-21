from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

app_name = "api_user"

urlpatterns = [
    path("signin/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", views.user_list, name="user_list"),
    path("<int:user_pk>/", views.user_detail, name="user_detail"),
    path("signup/", views.signup, name="signup"),
    path("profile/<int:user_pk>/", views.ProfileAPIView.as_view(), name="profile"),
]