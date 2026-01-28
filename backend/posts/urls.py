from django.urls import path
from .views import GetUserPostsView, PostCreateView , PostDetailView

urlpatterns = [
    path("", PostCreateView.as_view()),
    path("<int:post_id>/", PostDetailView.as_view()),
    path("user/<int:user_id>/", GetUserPostsView.as_view()),
]
