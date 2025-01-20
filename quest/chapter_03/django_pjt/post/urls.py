from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    # MTV
    path("", views.post_list, name="post_list"),
    path("post-create/", views.post_create, name="post_create"),
    path("post-detail/<int:pk>/", views.post_detail, name="post_detail"),
    path("post-update/<int:pk>/", views.post_update, name="post_update"),
    path("post-delete/<int:pk>/", views.post_delete, name="post_delete"),
    
    # DRF
    path("", views.PostListAPIView.as_view(), name="post_list"),
    path("<int:pk>/", views.PostDetailAPIView.as_view(), name="post_detail"),
    path("likes/<int:post_pk>/", views.LikesAPIView.as_view(), name="post_like"),
    path("<int:post_pk>/comments/", views.CommentListAPIView.as_view(), name="comment_list"),
    path("comments/<int:comment_pk>/", views.CommentDetailAPIView.as_view(), name="comment_detail"),
]