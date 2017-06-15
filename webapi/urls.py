from django.conf.urls import url
from rest_framework import routers
from .views import PhotoViewSet


router = routers.DefaultRouter()
router.register(r'photo', PhotoViewSet)
