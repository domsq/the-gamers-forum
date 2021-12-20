import random
import string
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DeleteView
from django.contrib import messages
from .models import Post, Topic
from .forms import PostAddForm, ReplyForm
from django.contrib.views.messages import SuccessMessageMixin


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


class PostAdd(SuccessMessageMixin, CreateView):
    model = Post
    fields = exclude('creator', 'created', 'updated')
    success_message = "successfully posted"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid()

class PostEdit(View):
    """ View to allow editing of existing posts """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'edit_post.html',
            {
                'post_edit_form': PostAddForm(instance=post)
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)

        post_edit_form = PostAddForm(request.POST, instance=post)

        if post_edit_form.is_valid():
            post_edit_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Post successfully amended!')

        else:
            post_edit_form = PostAddForm(instance=post)
            messages.add_message(request, messages.WARNING,
                                 'Post not amended. Please see ' +
                                 '"Guidance on editing posts."')

        return render(
            request,
            'edit_post.html',
            {
                'post_edit_form': PostAddForm(instance=post)
            }
        )


class PostDeleteView(DeleteView):
    model = Post
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return false
