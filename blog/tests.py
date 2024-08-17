from django.test import TestCase
from .models import Comment, Post
from django.contrib.auth.models import User

class CommentModelTest(TestCase):
    def setUp(self):
        # Creating a user for the test
        self.user = User.objects.create_user(username='testuser', password='password')

        # Creating a post that will be associated with the comment
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)

        # Creating a comment linked to the post and the user
        self.comment = Comment.objects.create(post=self.post, author=self.user, content='Test Comment')

    def test_comment_creation(self):
        # Check if the comment is created correctly
        self.assertEqual(self.comment.content, 'Test Comment')
        self.assertEqual(self.comment.author.username, 'testuser')
        self.assertEqual(self.comment.post.title, 'Test Post')

    def test_user_association(self):
        # Verify that the comment is associated with the correct user
        self.assertEqual(self.comment.author, self.user)

    def test_post_association(self):
        # Verify that the comment is associated with the correct post
        self.assertEqual(self.comment.post, self.post)

    def test_comment_count(self):
        # Verify that the post has the correct number of associated comments
        self.assertEqual(self.post.comments.count(), 1)
        # Add another comment to ensure count increases
        Comment.objects.create(post=self.post, author=self.user, content='Another Test Comment')
        self.assertEqual(self.post.comments.count(), 2)

    def test_string_representation(self):
        # Test the __str__ method of the comment
        expected_string = f"Comment by {self.user.username} on {self.post.title}"
        self.assertEqual(str(self.comment), expected_string)
