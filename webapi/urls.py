from django.conf.urls import url
from rest_framework import routers
from webapi import views

app_name = 'webapi'
urlpatterns = [
    url(r'^main_relation/(?P<uid>[0-9]+)$', views.get_main_relation),
    url(r'^model_relation/(?P<uid>[0-9]+)$', views.get_model_relation),
]

router = routers.DefaultRouter()
router.register(r'photo', views.PhotoViewSet)

