from django.contrib import admin
from .models import Topic, Post, Reply, Contact


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


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    """Admin view for Replies"""
    list_display = ('post', 'created', 'creator')
    search_fields = ('body', 'creator')
    list_filter = ('creator', 'created')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin view for messages sent to Contact"""
    list_display = ('fname', 'lname', 'email')
    search_fields = ('fname', 'lname', 'email', 'body')
    list_filter = ('fname', 'lname', 'email')
