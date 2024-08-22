from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LogDataViewSet

router = DefaultRouter()
router.register(f'logs', LogDataViewSet)


urlpatterns = [
    path('', include(router.urls))
]
