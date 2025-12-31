from rest_framework import serializers
from .models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("text", "reply_to")

    def validate_text(self, value: str) -> str:
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Text cannot be empty.")
        if len(value) > 500:
            raise serializers.ValidationError("Text too long (max 500).")
        return value


class PostReadSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ("id", "text", "created_at", "author", "reply_to")

    def get_author(self, obj):
        return {
            "id": obj.author_id,
            "handle": obj.author.handle,
            "avatar_url": obj.author.avatar_url,
        }