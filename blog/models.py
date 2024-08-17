"""
Module containing the models for the blog application.
"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=400, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """
        Metadata for controlling the default ordering of posts.
        """
        ordering = ['-created_on']
    
    def __str__(self):
        """
        Return a string representation of the post title.
        """
        return self.title

    def number_of_likes(self):
        """
        Return the number of likes for the post.
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Model representing a comment on a blog post.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Metadata for controlling the default ordering of comments.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Return a string representation of the comment.
        """
        return f'{self.name}: {self.body[:20]}'
        # return f"Comment {self.body} by {self.name}"
