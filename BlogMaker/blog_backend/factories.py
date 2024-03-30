import factory
from factory import Faker
from factory.django import DjangoModelFactory
from .models import BlogPost

class BlogPostFactory(DjangoModelFactory):
    class Meta:
        model = BlogPost

    title = Faker('sentence')
    content = Faker('text')