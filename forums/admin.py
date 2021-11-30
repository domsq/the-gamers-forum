from django.contrib import admin
from .models import Topic, Post


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """Admin view for Topics"""
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin view for Posts"""
    list_display = ('title', 'slug', 'created', 'creator')
    search_fields = ('title', 'body', 'creator')
    list_filter = ('creator', 'created')
