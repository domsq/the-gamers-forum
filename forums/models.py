from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Topic(models.Model):
    """Schema for the Topic model"""
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    """Schema for the Post model"""
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name="user_posts")
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField("image", default="placeholder")
    upvote = models.ManyToManyField(User, related_name="post_upvotes",
                                    blank=True)
    downvote = models.ManyToManyField(User, related_name="post_downvotes",
                                      blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,
                              related_name="topic_posts")

    def __str__(self):
        return self.title

    def number_of_upvotes(self):
        """Returns number of upvotes as a total"""
        return self.upvote.count()

    def number_of_downvotes(self):
        """Returns number of downvotes as a total"""
        return self.downvote.count()

    class Meta:
        """Sorts the posts in descending order"""
        ordering = ["-created"]


class Reply(models.Model):
    """Schema for the Reply model"""
    body = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name="user_replies")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = CloudinaryField("image", default="placeholder")
    upvote = models.ManyToManyField(User, related_name="reply_upvotes",
                                    blank=True)
    downvote = models.ManyToManyField(User, related_name="reply_downvotes",
                                      blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="post_replies")

    def __str__(self):
        return f"Reply {self.body} by {self.creator}"

    def number_of_upvotes(self):
        """Returns number of upvotes as a total"""
        return self.upvote.count()

    def number_of_downvotes(self):
        """Returns number of downvotes as a total"""
        return self.downvote.count()

    class Meta:
        """Sorts the posts in descending order"""
        ordering = ["-created"]
