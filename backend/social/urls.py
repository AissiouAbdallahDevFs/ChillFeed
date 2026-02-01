from django.urls import path
from .views import FollowView, UnfollowView , LikeView, UnlikeView

urlpatterns = [
    path("follow/", FollowView.as_view()),
    path("unfollow/", UnfollowView.as_view()),
    path("like/", LikeView.as_view()),
    path("unlike/", UnlikeView.as_view()),
]
