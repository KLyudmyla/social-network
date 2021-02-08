
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from likes.models import Like
from likes.serializers import LikeSerializer
from likes.utils import get_date
from posts.views import ReadOnly
from datetime import date


class Likes(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated | ReadOnly,)


class LikeAnalytics(APIView):

    @permission_classes((permissions.IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        date_from_day, date_from_month, date_from_year = get_date(request, "dateFrom")
        date_to_day, date_to_month, date_to_year = get_date(request, "dateTo")
        amount_of_likes = len(
            Like.objects.filter(created_date__gte=date(date_from_year, date_from_month, date_from_day),
                                created_date__lte=date(date_to_year, date_to_month, date_to_day)))
        return Response({
            'amount of likes': amount_of_likes,
        }, status=status.HTTP_200_OK)
