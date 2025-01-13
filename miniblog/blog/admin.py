from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']

admin.site.register(Post)