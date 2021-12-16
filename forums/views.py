from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Post, Topic
from .forms import ReplyForm


class TopicList(generic.ListView):
    """ View to render the topics list """
    model = Topic
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(TopicList, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-created')
        return context


class TopicDetail(View):
    """ View to render detail for a chosen topic """
    def get(self, request, name, *args, **kwargs):
        queryset = Topic.objects
        topic = get_object_or_404(queryset, name=name)
        posts = topic.topic_posts.order_by('-created')

        return render(
            request,
            'topic_detail.html',
            {
                "topic": topic,
                "posts": posts
            },
        )


class PostDetail(View):
    """ View to render detail for a chosen post """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        replies = post.post_replies.order_by('-created')

        return render(
            request,
            'post_detail.html',
            {
                "post": post,
                "replies": replies,
                "reply_form": ReplyForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        replies = post.post_replies.order_by('-created')

        reply_form = ReplyForm(data=request.POST)

        if reply_form.is_valid():
            reply_form.instance.creator = request.user
            reply = reply_form.save(commit=False)
            reply.post = post
            reply.save()

        else:
            reply_form = ReplyForm()

        return render(
            request,
            'post_detail.html',
            {
                "post": post,
                "replies": replies,
                "reply_form": ReplyForm()
            },
        )
