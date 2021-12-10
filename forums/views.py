from django.shortcuts import render
from django.views import generic
from .models import Topic


class TopicList(generic.ListView):
    """ View to render the topics list """
    model = Topic
    queryset = Topic.objects.order_by('name')
    template_name = 'index.html'
    paginate_by = 6

