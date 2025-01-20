from django.urls import path
from . import views

app_name = "api_post"

urlpatterns = [
    path("", views.PostListAPIView.as_view(), name="api_post_list"),
    path("<int:post_pk>/", views.PostDetailAPIView.as_view(), name="api_post_detail"),
]