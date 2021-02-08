from django.urls import include, path
from rest_framework import routers
from users import views


router = routers.DefaultRouter()
router.register(r'', views.Users)


urlpatterns = [
    path('', include(router.urls)),
    path('account/register', views.UserRegistration.as_view()),
    path('last_activity', views.UserLastActivity.as_view())
]
