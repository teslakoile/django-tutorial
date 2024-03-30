from django.contrib import admin
from .models import BlogPost

# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'snippet')
    readonly_fields = ('id', 'created_at', 'updated_at', 'snippet')
    
    def snippet(self, obj):
        """
        Returns the snippet property of the BlogPost object.
        """
        return obj.snippet