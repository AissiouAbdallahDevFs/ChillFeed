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
            {"id": post.id, "created_at": post.created_at.isoformat()},
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
