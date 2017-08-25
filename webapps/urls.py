from django.conf.urls import url
from . import views


app_name = 'webapps'
urlpatterns = [
    # ex: /webapps/
    url(r'^$', views.index, name='index'),
    # ex: /webapps/5/
    url(r'^(?P<photo_uid>[0-9]+)/$', views.detail, name='detail'),
    url(r'^relation/(?P<photo_uid>[0-9]+)/$', views.relation, name='relation'),
]
