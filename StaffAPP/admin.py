from django.contrib import admin
from .models import BlogModel

# Register your models here.
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'title', 'short_description', 'author', 'status', 'created_at']

admin.site.register(BlogModel, BlogModelAdmin)