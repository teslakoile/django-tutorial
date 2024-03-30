from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from .models import BlogPost
from .serializers import BlogPostDetailSerializer, BlogPostListSerializer


# Create your views here.
class BlogPostListView(GenericAPIView):
    """
    View for listing and creating blog posts.
    """

    serializer_class = BlogPostListSerializer
    permission_classes = [AllowAny]
    queryset = BlogPost.objects.all()

    def get(self, request: Request) -> Response:
        blog_posts = self.get_queryset()
        serializer = self.get_serializer(blog_posts, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostDetailView(GenericAPIView):
    """
    View for retrieving a single blog post.
    """

    serializer_class = BlogPostDetailSerializer
    permission_classes = [AllowAny]

    def get_object(self, blog_post_id):
        """
        Get the BlogPost instance with the given ID. Return a 404 response if the blog post does not exist.
        """
        try:
            return BlogPost.objects.get(id=blog_post_id)
        except BlogPost.DoesNotExist:

            raise NotFound(detail="Blog post does not exist")

    def get(self, request: Request, blog_post_id: int) -> Response:
        blog_post = self.get_object(blog_post_id)
        serializer = self.get_serializer(blog_post)

        return Response(serializer.data)

    def patch(self, request: Request, blog_post_id: int) -> Response:
        blog_post = self.get_object(blog_post_id)
        serializer = self.get_serializer(blog_post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, blog_post_id: int) -> Response:
        blog_post = self.get_object(blog_post_id)
        blog_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
