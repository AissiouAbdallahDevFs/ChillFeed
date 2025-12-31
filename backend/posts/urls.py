from django.urls import path
from .views import PostCreateView , PostDetailView

urlpatterns = [
    path("", PostCreateView.as_view()),
    path("<int:post_id>/", PostDetailView.as_view()),
]
