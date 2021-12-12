from django.shortcuts import render
from django.views import generic
from .models import Post, Topic


class TopicList(generic.ListView):
    """ View to render the topics list """
    model = Topic
    template_name = 'index.html'    

    def get_context_data(self, **kwargs):
        context = super(TopicList, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-created')
        return context
