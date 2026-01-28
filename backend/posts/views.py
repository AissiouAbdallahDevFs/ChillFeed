from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Post
from .serializers import PostCreateSerializer , PostReadSerializer
from django.shortcuts import get_object_or_404


class PostCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post = Post.objects.create(
            author=request.user,
            text=serializer.validated_data["text"],
            reply_to=serializer.validated_data.get("reply_to"),
        )

        return Response(
            {"id": post.id, "created_at": post.created_at.isoformat(),"Post": post.text},
            status=status.HTTP_201_CREATED,
        )
    
class PostDetailView(APIView):
    def get(self, request, post_id: int):
        post = get_object_or_404(
            Post.objects.select_related("author"),
            id=post_id,
            is_deleted=False,
        )
        return Response(PostReadSerializer(post).data)


class GetUserPostsView(APIView):
    def get(self, request, user_id: int):
        posts = Post.objects.filter(
            author_id=user_id,
            is_deleted=False,
        ).select_related("author").order_by("-created_at")

        serializer = PostReadSerializer(posts, many=True)
        return Response(serializer.data)
    
class GetAllPostsView(APIView):
    def get(self, request):
        posts = Post.objects.filter(
            is_deleted=False,
        ).select_related("author").order_by("-created_at")

        serializer = PostReadSerializer(posts, many=True)
        return Response(serializer.data)

class DeletePostView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, post_id: int):
        post = get_object_or_404(Post, id=post_id, is_deleted=False)
        if post.author != request.user:
            return Response(
                {"detail": "You do not have permission to delete this post."},
                status=status.HTTP_403_FORBIDDEN,
            )
        post.is_deleted = True
        post.save()

        return Response(status=status.HTTP_204_NO_CONTENT ,message="Post deleted successfully.")
    
class EditPostView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, post_id: int):
        post = get_object_or_404(Post, id=post_id, is_deleted=False)
        if post.author != request.user:
            return Response(
                {"detail": "You do not have permission to edit this post."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = PostCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post.text = serializer.validated_data["text"]
        post.save()

        return Response(
            {"id": post.id, "created_at": post.created_at.isoformat(), "text": post.text , "message": "Post updated successfully."},
            status=status.HTTP_200_OK,
        )