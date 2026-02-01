from django.contrib import admin
from .models import Follow, Like, Repost


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("id", "follower", "followee", "created_at")
    search_fields = ("follower__email", "follower__handle", "followee__email", "followee__handle")
    list_filter = ("created_at",)
    ordering = ("-created_at",)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "created_at")
    search_fields = ("user__email", "user__handle")
    list_filter = ("created_at",)
    ordering = ("-created_at",)


@admin.register(Repost)
class RepostAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "created_at")
    search_fields = ("user__email", "user__handle")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
