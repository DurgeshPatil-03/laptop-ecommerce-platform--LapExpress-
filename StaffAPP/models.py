from django.db import models

class BlogModel(models.Model):
    image = models.ImageField(upload_to='media/', default='Not Uploaded')
    title = models.CharField(max_length=200, default='No Title')
    short_description = models.CharField(max_length=300, default='No Description')
    author = models.CharField(max_length=100, default='Anonymous')
    status = models.BooleanField(default=True)
    content = models.TextField(default='No Content')
    created_at = models.DateTimeField(auto_now_add=True)