from django.urls import path
from . import views


app_name = "user"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("user_profile/", views.user_profile, name="user_profile"),
]