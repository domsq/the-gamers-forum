from .models import Reply
from django import forms


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('body',)
