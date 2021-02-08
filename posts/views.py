
from posts.serializers import PostSerializer
from posts.models import Post

from rest_framework import viewsets, permissions, status
from rest_framework.permissions import BasePermission, IsAuthenticated


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method == "GET"


class Posts(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated | ReadOnly,)
