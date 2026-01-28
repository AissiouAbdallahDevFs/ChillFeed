from django.urls import path
from .views import GetAllPostsView, GetUserPostsView, PostCreateView , PostDetailView, DeletePostView

urlpatterns = [
    path("", PostCreateView.as_view()),
    path("<int:post_id>/", PostDetailView.as_view()),
    path("user/<int:user_id>/", GetUserPostsView.as_view()),
    path("posts/", GetAllPostsView.as_view()),
    path("delete/<int:post_id>", DeletePostView.as_view()),
]
