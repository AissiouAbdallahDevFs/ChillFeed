from rest_framework import serializers
from users.models import User 
from posts.models import Post


class FollowSerializer(serializers.Serializer):
    handle = serializers.CharField(max_length=32)

    def validate_handle(self, value):
        try:
            user = User.objects.get(handle=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")
        return user


class LikeSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()

    def validate_post_id(self, value):
        try:
            post = Post.objects.get(id=value, is_deleted=False)
        except Post.DoesNotExist:
            raise serializers.ValidationError("Post not found.")
        return post