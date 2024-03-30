from django.urls import reverse
from icecream import ic
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import BlogPostFactory
from .models import BlogPost
from .serializers import BlogPostDetailSerializer, BlogPostListSerializer


# Create your tests here.
class BlogPostTestCase(APITestCase):
    """
    Test cases for the BlogPost endpoints.
    """

    @classmethod
    def setUpTestData(cls) -> None:
        cls.blog_posts = BlogPostFactory.create_batch(10)
        cls.list_url = reverse("blogpost-list")

    def test_list_blog_posts(self):
        """
        Test that the list of blog posts is returned correctly.
        """
        response = self.client.get(self.list_url)

        blog_posts = BlogPost.objects.all()
        serializer = BlogPostListSerializer(blog_posts, many=True)
        expected_data = serializer.data

        ic(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), BlogPost.objects.count())
        self.assertEqual(response.json(), expected_data)

    def test_get_blog_post(self):
        """
        Test that the first blog post is returned correctly.
        """
        first_blog_post = BlogPost.objects.first()
        self.detail_url = reverse(
            "blogpost-detail", kwargs={"blog_post_id": first_blog_post.id}
        )
        response = self.client.get(self.detail_url)

        serializer = BlogPostDetailSerializer(first_blog_post)
        expected_data = serializer.data

        ic(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected_data)

    def test_create_blog_post(self):
        """
        Test that a new blog post is created correctly.
        """
        request_body = {"title": "New Blog Post", "content": "This is a new blog post"}
        response = self.client.post(self.list_url, request_body, format="json")

        new_blog_post = BlogPost.objects.latest("id")
        serializer = BlogPostListSerializer(new_blog_post)
        expected_data = serializer.data

        ic(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), expected_data)
