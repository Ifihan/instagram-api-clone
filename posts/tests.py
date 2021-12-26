from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from posts.models import Post, Image
from accounts.models import AppUser
from posts.serializers import PostsSerializer, ImageSerializer

# Create your tests here.
class CreatePostTestCase(APITestCase):

    url = reverse("posts:post")

    def setUp(self):
        self.user = AppUser.objects.create(
            username="fritz",
            password="fritz123@",
            email="fritz@gmail.com",
            first_name="Fritz",
            last_name="Konsan",
            phone_number="+2348123456789")

    def test_create_post(self):
        response = self.client.post(self.url, {"caption": "Hello World"})
        self.assertEqual(response.status_code, 201)

    

    