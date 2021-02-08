from django.contrib.auth.models import User

from users.serializers import UserSerializer, UserRegistrationSerializer

from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpRequest

import logging

logger = logging.getLogger(__name__)


class Users(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


class UserDetail(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @permission_classes((permissions.IsAuthenticated,))
    def delete(self, request, *args, **kwargs):
        user_profile = self.get_object()
        User.objects.get(title=user_profile.title).delete()
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny, )


class UserLastActivity(APIView):
    @permission_classes((permissions.IsAuthenticated,))
    def get(self, request: HttpRequest):
        last_login = self.request.user.last_login
        last_request = self.request.user.user_profile.last_activity
        return Response({
            'last_login': last_login,
            'last_request': last_request,
        })
