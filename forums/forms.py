from .models import Post, Reply
from django import forms


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('body',)


class PostAddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('topic', 'title', 'body',)
