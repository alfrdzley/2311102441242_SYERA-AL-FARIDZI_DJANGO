from django.db import models


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=600)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)