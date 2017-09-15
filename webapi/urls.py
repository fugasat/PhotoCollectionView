from django.conf.urls import url
from rest_framework import routers
from webapi import views

app_name = 'webapi'
urlpatterns = [
    url(r'^(?P<uid>[0-9]+)/(?P<relation_type>[0-9]+)/(?P<history>[0-9x]+)/$', views.get_relation),
]

router = routers.DefaultRouter()
router.register(r'photo', views.PhotoViewSet)

