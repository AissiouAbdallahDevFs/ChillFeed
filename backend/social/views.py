from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Follow , Like , Repost
from .serializers import FollowSerializer , LikeSerializer , RepostSerializer


class FollowView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FollowSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        followee = serializer.validated_data["handle"]
        follower = request.user

        if follower == followee:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Follow.objects.get_or_create(
            follower=follower,
            followee=followee,
        )

        return Response({"detail": "Followed."}, status=status.HTTP_201_CREATED)


class UnfollowView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FollowSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        followee = serializer.validated_data["handle"]
        follower = request.user

        Follow.objects.filter(
            follower=follower,
            followee=followee,
        ).delete()

        return Response({"detail": "Unfollowed."}, status=status.HTTP_200_OK)



class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.validated_data["post_id"]
        user = request.user
        Like.objects.get_or_create(user=user, post=post)

        return Response({"detail": "Liked."}, status=status.HTTP_201_CREATED)


class UnlikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post = serializer.validated_data["post_id"]
        user = request.user

        Like.objects.filter(user=user, post=post).delete()

        return Response({"detail": "Unliked."}, status=status.HTTP_200_OK)
    


class RepostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RepostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post = serializer.validated_data["post_id"]
        user = request.user

        Repost.objects.get_or_create(user=user, post=post)

        return Response({"detail": "Reposted."}, status=status.HTTP_201_CREATED)


class UnrepostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RepostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post = serializer.validated_data["post_id"]
        user = request.user

        Repost.objects.filter(user=user, post=post).delete()

        return Response({"detail": "Unreposted."}, status=status.HTTP_200_OK)