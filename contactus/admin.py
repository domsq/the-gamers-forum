from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin view for messages sent to Contact"""
    list_display = ('fname', 'lname', 'email', 'created')
    search_fields = ('fname', 'lname', 'email', 'body')
    list_filter = ('fname', 'lname', 'email')
