from django.urls import path
from . import views

app_name = "api_post"

urlpatterns = [
    path("", views.PostListAPIView.as_view(), name="api_post_list"),
    path("<int:post_pk>/", views.PostDetailAPIView.as_view(), name="api_post_detail"),
    path("likes/<int:post_pk>/", views.LikesAPIView.as_view(), name="api_post_like"),
    path("<int:post_pk>/comments/", views.CommentListAPIView.as_view(), name="api_comment_list"),
    path("comments/<int:comment_pk>/", views.CommentDetailAPIView.as_view(), name="api_comment_detail"),
]