from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "handle", "is_active", "is_staff", "date_joined")
    search_fields = ("email", "handle")
    list_filter = ("is_active", "is_staff")
    ordering = ("-date_joined",)
