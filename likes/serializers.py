from rest_framework import serializers

from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('url', 'post', 'like', 'user')

    def create(self, validated_data):
        validated_data["user"] = self.context['request'].user
        like = Like(**validated_data)
        like.save()
        return like
