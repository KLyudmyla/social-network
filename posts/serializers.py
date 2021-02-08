from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'author', 'text')

    def create(self, validated_data):
        validated_data["author"] = self.context['request'].user
        post = Post(**validated_data)
        post.save()
        return post
