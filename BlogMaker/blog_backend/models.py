from django.db import models

# Create your models here.
class BlogPost(models.Model):
    """
    Model for a blog post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def snippet(self):
        """
        Returns the first 50 characters of the content if the content is longer than 50 characters.
        """
        return self.content[:50] if len(self.content) > 50 else self.content