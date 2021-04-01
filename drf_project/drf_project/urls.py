from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter

from drf_project.Auth import views
from drf_project.Auth.auth import CustomAuthToken

router = DefaultRouter()

router.register('Auth', views.StudentView, basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', CustomAuthToken.as_view(), name='token_obtain_pair')
]
