from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# from django_timestamps.softDeletion import SoftDeletionModel
# from django_timestamps.timestamps import TimestampsModel
from django.utils.translation import gettext_lazy as _




class User(AbstractUser):
    """User model."""

    
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # objects = BaseUserManager()