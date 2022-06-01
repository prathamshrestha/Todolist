from email.mime import image
from django.db import models
from django_timestamps.softDeletion import SoftDeletionModel
from django_timestamps.timestamps import TimestampsModel
from django.conf import settings
User=settings.AUTH_USER_MODEL

def upload_path(instance, filename):
    return '/'.join(['todo',str(instance.name), filename])

class Todolist_model(SoftDeletionModel, TimestampsModel):
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    name=models.CharField(max_length=255)
    todo_image=models.ImageField(blank=True, upload_to=upload_path)
    description=models.CharField(max_length=510)
    deadline=models.DateTimeField(blank=True,null=True)

    creation_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


