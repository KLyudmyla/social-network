from django.urls import include, path
from rest_framework import routers

from posts import views

router = routers.DefaultRouter()
router.register(r'', views.Posts)

urlpatterns = (
    path('', include(router.urls)),
)
