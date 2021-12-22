from django import forms
from .models import Post, Reply


class ReplyForm(forms.ModelForm):
    """ Form for posting replies """
    class Meta:
        model = Reply
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }


class PostAddForm(forms.ModelForm):
    """ Form for adding or editing posts """
    class Meta:
        model = Post
        fields = ('topic', 'title', 'body',)
