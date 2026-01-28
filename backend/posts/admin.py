from django.contrib import admin
from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "created_at", "is_deleted")
    search_fields = ("text", "author__email", "author__handle")
    list_filter = ("is_deleted", "created_at")
    ordering = ("-created_at",)