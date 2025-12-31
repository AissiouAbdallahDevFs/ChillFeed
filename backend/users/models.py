from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    handle = models.CharField(max_length=32, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
    avatar_url = models.URLField(blank=True, default="")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['handle']

    objects = UserManager()

    def __str__(self):
        return self.handle