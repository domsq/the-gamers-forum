from django.contrib import admin
from .models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """Admin view for Topics"""
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
