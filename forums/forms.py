from django import forms
from .models import Post, Reply


class ReplyForm(forms.ModelForm):
    """ Form for posting replies """
    class Meta:
        model = Reply
        fields = ('body',)


class PostAddForm(forms.ModelForm):
    """ Form for adding or editing posts """
    class Meta:
        model = Post
        fields = ('topic', 'title', 'body',)
