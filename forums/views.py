from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from .models import Post, Topic
from .forms import PostAddForm, ReplyForm


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
            messages.add_message(request, messages.SUCCESS,
                                 'Reply successfully added!')

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

class PostAdd(View):
    """ View to allow adding of new posts """
    def get(self, request, *args, **kwargs):

        return render(
            request,
            'add_post.html',
            {
                'post_add_form': PostAddForm()
            }
        )

    def post(self, request, *args, **kwargs):

        post_add_form = PostAddForm(data=request.POST)

        if post_add_form.is_valid():
            post_add_form.instance.creator = request.user
            post_add_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Post successfully added!')

        else:
            post_add_form = PostAddForm()
            messages.add_message(request, messages.WARNING,
                                 'Post not added. Please see ' +
                                 '"Guidance on creating posts."')

        return render(
            request,
            'add_post.html',
            {
                'post_add_form': PostAddForm()
            }
        )
