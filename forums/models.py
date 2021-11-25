from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Topic(models.Model):
    """Schema for the Topic model"""
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
