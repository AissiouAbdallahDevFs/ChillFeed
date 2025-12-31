from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # tu pourras ajouter handle, avatar, bio plus tard
    pass