from django.urls import include, path
from rest_framework import routers


from likes import views

router = routers.DefaultRouter()
router.register('', views.Likes)


urlpatterns = (
    path('', include(router.urls)),
    path('analytics', views.LikeAnalytics.as_view()),
)
