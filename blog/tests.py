from django.test import TestCase, Client
from .models import Post,Comment 
from django.utils import timezone
from django.core.urlresolvers import reverse
from .forms import *




class AvailabilityofLocalhost(TestCase):

    def test_homepage_available(self):
        c = Client()
        response = c.get('/')
        self.assertEquals(response.status_code, 200)

'''

class PostViewTestCase(TestCase):                    #Only for post with id 15
    def test_post_creation(self):
        c = Client()  # instantiate the Django test client
        response = c.post('/post/new', {'title': 'Some title', 'text': 'Some text'})
        self.assertEqual(response, [('/post/15/', 302)])
        self.assertContains(response, 'Post created.')
        self.assertContains(response, 'Some title')
'''

class Setup_Class(TestCase):

    def setUp(self):
        self.Post = Post.objects.create(title = "new post", text="new text")

class Post_Form_Test(TestCase):

    # Valid Form Data
    def test_PostForm_valid(self):
        form = PostForm(data={'title': "some title", 'text': "some text"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_PostForm_invalid(self):
        form = PostForm(data={'title': "", 'text': ""})




class Setup_Class(TestCase):

    def setUp(self):
        self.Comment = Comment.objects.create(name = "name", email="email@email.com", body = "Comment")

class Comment_Form_Test(TestCase):

    # Valid Form Data
    def test_CommentForm_valid(self):
        form = CommentForm(data={'name': "seva", 'email': "vsevolod.shutyuk@mail.ru", 'body':"Great article"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_CommentForm_invalid(self):
        form = PostForm(data={'name': "", 'email': "", 'body':""})

