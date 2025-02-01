from django.urls import path
from . import views

app_name = "api_openai"

urlpatterns = [
    path("docs/", views.OpenAIDocsAPIViews.as_view()),
]