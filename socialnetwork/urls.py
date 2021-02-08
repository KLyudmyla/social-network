
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/posts/', include('posts.urls')),
    path('api/v1/likes/', include('likes.urls')),
    path('api/v1/api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
