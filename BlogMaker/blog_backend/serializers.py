from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "snippet"]
        read_only_fields = ["id", "snippet"]

    def validate(self, attrs):
        """
        Check that the title is not "Test".
        """
        title = attrs.get("title", "")
        if title.lower() == "test":
            raise serializers.ValidationError("Title cannot be 'Test'")
        return attrs


class BlogPostListSerializer(BlogPostSerializer):
    def create(self, validated_data):
        """
        Custom create method that prefixes the title with "Blog Post: " if it doesn't already start with it.
        """
        title = validated_data.get("title", "")
        if not title.startswith("Blog Post: "):
            validated_data["title"] = f"Blog Post: {title}"

        return BlogPost.objects.create(**validated_data)


class BlogPostDetailSerializer(BlogPostSerializer):
    class Meta(BlogPostSerializer.Meta):
        fields = BlogPostSerializer.Meta.fields + ["created_at", "updated_at"]
        read_only_fields = ["id", "snippet", "created_at", "updated_at"]

    def update(self, instance, validated_data):
        """
        Update the BlogPost instance. If the title is updated, append "[Updated]" at the end.
        """
        new_title = validated_data.get("title")

        if (
            new_title
            and new_title != instance.title
            and not new_title.endswith("[Updated]")
        ):
            instance.title = f"{new_title} [Updated]"
        else:
            instance.title = new_title or instance.title

        instance.content = validated_data.get("content", instance.content)
        instance.save()

        return instance
