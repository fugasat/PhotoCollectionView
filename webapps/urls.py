from django.conf.urls import url
from . import views


app_name = 'webapps'
urlpatterns = [
    # ex: /webapps/
    url(r'^$', views.index, name='index'),
    # ex: /webapps/5/
    url(r'^(?P<photo_uid>[0-9]+)/$', views.detail, name='detail'),
    # ex: /webapps/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /webapps/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
