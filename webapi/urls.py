from django.conf.urls import url
from rest_framework import routers
from webapi import views

app_name = 'webapi'
urlpatterns = [
    url(r'^api/relation/(?P<pre_uid>[0-9]+)/(?P<uid>[0-9]+)/(?P<relation_type>[0-9]+)/$', views.get_relation),
    url(r'^api/relation/(?P<history>[0-9x]+)/$', views.get_relation_from_history),
]

router = routers.DefaultRouter()
router.register(r'photo', views.PhotoViewSet)

