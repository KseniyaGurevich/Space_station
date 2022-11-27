from django.urls import include, path
from .views import StationViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'stations', StationViewSet, basename='stations')

urlpatterns = [
    path('', include(router.urls)),
    path(r'auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
