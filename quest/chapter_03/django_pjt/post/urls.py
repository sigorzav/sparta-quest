from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post-detail/<int:pk>/", views.post_detail, name="post_detail"),
    path("post-delete/<int:pk>/", views.post_delete, name="post_delete"),
]