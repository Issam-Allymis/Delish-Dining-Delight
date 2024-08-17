"""
Module containing views for the blog application.
"""

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    """View for displaying a list of posts."""
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """
    View for handling post likes.

    Handles POST requests.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Handle POST requests to like/unlike a post.
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """Handle POST requests."""
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment was submitted successfully. Thank you for your feedback!')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class PostLike(View):
    """View for handling post likes."""
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

@login_required
def update_comment(request, comment_id):
    """View for handling comment editing."""
    comment = get_object_or_404(Comment, id=comment_id)

    # Debugging output
    print(f"Comment post slug: {comment.post.slug}")

    # Check if the logged-in user is the author of the comment
    if request.user.username != comment.name:
        messages.error(request, "You are not authorized to edit this comment.")
        return redirect('post_detail', slug=comment.post.slug)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment was updated successfully.')
            return redirect('post_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'update_comment.html', {'form': form})

@login_required
def delete_comment(request, comment_id):
    """View for handling comment deletion."""
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the logged-in user is the author of the comment
    if request.user.username != comment.name:
        messages.error(request, "You are not authorized to delete this comment.")
        return redirect('post_detail', slug=comment.post.slug)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Your comment was deleted successfully.')
        return redirect('post_detail', slug=comment.post.slug)

    return render(request, 'delete_comment.html', {'comment': comment})