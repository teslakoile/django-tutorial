from django.urls import path

from . import views

urlpatterns = [
    path("blogposts", views.BlogPostListView.as_view(), name="blogpost-list"),
    path(
        "blogposts/<int:blog_post_id>",
        views.BlogPostDetailView.as_view(),
        name="blogpost-detail",
    ),
]
