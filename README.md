# Django Tutorial Setup Guide

This guide provides a comprehensive walkthrough to set up and run a Django application. It covers everything from the initial setup, including the installation of necessary software and tools, to the configuration of a Django project with the Django Rest Framework. 

The guide is designed to help both beginners and experienced developers navigate the Django Rest Framework. It includes detailed instructions for creating a virtual environment, installing Django and Django Rest Framework, setting up a new Django project and application, and running the development server. 

In addition to the setup and running of the application, this guide also provides insights into creating models, views, and serializers, defining URL patterns, writing test cases, and registering models with the Django admin interface. 

By following this guide, you will have a fully functional Django application up and running, ready for further development and deployment.

## Prerequisites

- Python 3.8 or higher
- pip 
- git

## Setup Instructions

1. **Create and Navigate to Your Project Directory**:

```
mkdir django-tutorial
cd django-tutorial
```

2. **Initialize Git Repository**:
```
git init
```

3. **Create a Virtual Environment**:
```
python -m venv venv
```

4. **Activate the virtual environment**:
```
source venv/bin/activate
```

5. **Install Django and Django Rest Framework**:

```
pip install django
pip install djangorestframework
```

6. **Create a New Django Project**:

```
django-admin startproject BlogMaker
cd BlogMaker
```

7. **Make Migrations and Migrate**:

This prepares and applies the initial database migrations.

```
python manage.py makemigrations
python manage.py migrate
```

8. **Collect Static Files**:

In the settings.py file inside the BlogMaker directory, add the following line to set your static root.

```
STATIC_ROOT = os.path.join(BASE_DIR, "static")
```

Collect your static files.

```
python manage.py collectstatic
```

9. **Create a Django App**:

```
python manage.py startapp blog_backend
```

Add `rest_framework` and the `blog_backend` app to the `INSTALLED_APPS` in your settings file

```
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "blog_backend",
]
```

10. **Create a Superuser**:

```
python manage.py createsuperuser
```

Determine the superuser credentials. You can use this to login to the admin site.

11. **Run the Development Server**:

```
python manage.py runserver
```

Access the application at http://localhost:8000/.

12. **Creating Models**:

Define your models in `models.py` within your `blog_backend` app directory.

```
class BlogPost(models.Model):
    """
    Model for a blog post.
    """
```

After creating models, generate migrations and apply them:

```
python manage.py makemigrations
python manage.py migrate
```

13. **Create Serializers**:


Create a `serializers.py` file within your `blog_backend` app. Define your serializers in `serializers.py` within your `blog_backend` app directory to handle data conversion for your models.

```
class BlogPostSerializer(serializers.ModelSerializer):

class BlogPostListSerializer(BlogPostSerializer):

class BlogPostDetailSerializer(BlogPostSerializer):
```

14. **Create Views**:

Implement your views in `views.py` within your `blog_backend` app directory, utilizing Django and Django Rest Framework classes.

```
class BlogPostListView(GenericAPIView):
    """
    View for listing and creating blog posts.
    """


class BlogPostDetailView(GenericAPIView):
    """
    View for retrieving a single blog post.
    """
```

15. **Adjust URL Patterns**:

Define URL patterns in `urls.py` within your `blog_backend` app directory to route your views.

```
urlpatterns = [
    path("blogposts", views.BlogPostListView.as_view(), name="blogpost-list"),
```

Additionally, in your BlogMaker/urls.py file, add the following line to add an api/ prefix and include the URL patterns from your blog_backend app:

```
path("api/", include("blog_backend.urls")),
```

16. **Add Test Factories and Unit Tests**:

Install factory_boy and create a `factories.py` folder

```
pip install factory_boy
```

Write test cases in `tests.py` within your app directory to ensure your application behaves as expected.

```
class BlogPostTestCase(APITestCase):
    """
    Test cases for the BlogPost endpoints.
    """

    @classmethod
    def setUpTestData(cls) -> None:
```

To run the unit tests, use the following management command

```
python manage.py test blog_backend.tests   
```

17. **Register Models with Admin**:

Add your models to admin.py within your app directory to manage them through the Django admin interface.

```
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
```


# Application Overview

This Django application provides a few general endpoints for listing, creating, and retrieving blog posts. Below is an overview of the available endpoints and their functionality.

## Application Endpoints

### Blog Posts List and Create

- **URL**: `/api/blogposts`
- **Method**: `GET`
- **Description**: Retrieve a list of all blog posts.
- **Response**: An array of blog posts, each including the title, content, and a snippet.

- **URL**: `/api/blogposts`
- **Method**: `POST`
- **Description**: Create a new blog post.
- **Request Body**:
```
{
    "title": "Your Blog Post Title",
    "content": "The content of your blog post."
}
```
- **Response**: The created blog post object, including its ID, title, content, and a snippet.
```
{
    "id": 1,
    "title": "Your Blog Post Title",
    "content": "The content of your blog post.",
    "snippet": "The content of your blog post."
}
```

### Blog Post Detail
- **URL**: `/api/blogposts/<int:blog_post_id>`
- **Method**: GET
- **Description**: Retrieve a detailed view of a single blog post by its ID.
- **URL Parameters**: blog_post_id - An integer representing the unique ID of the blog post.
- **Response**: The blog post object, including its ID, title, content, created and updated timestamps, and a snippet.
```
{
    "id": 1,
    "title": "Your Blog Post Title",
    "content": "The content of your blog post.",
    "snippet": "The content of your blog post.",
    "created_at": "2024-03-30T12:48:08.602674Z",
    "updated_at": "2024-03-30T12:59:56.110330Z"
}
```

## BlogPost Model
- **id (Integer)**: A unique identifier for each blog post.
- **title (String)**: The title of the blog post.
- **content (Text)**: The content/body of the blog post.
- **created_at (DateTime)**: The timestamp when the blog post was created.
- **updated_at (DateTime)**: The timestamp when the blog post was last updated.
- **snippet (String)**: A property that returns the first 50 characters of the content.

## Running the Application
Follow the setup instructions provided above to get the application up and running. Once the application is running, you can interact with the API endpoints through tools like Postman.
```
python manage.py runserver
```

## Running Unit Tests
```
python manage.py test blog_backend.tests   
```