from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import PhotoSerializer
from webapps.models import Photo
from webapps.features import Features

__features = Features("instagram_data_all.csv")


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

@api_view(['GET'])
def get_main_relation(request, uid):
    print("view photo : {0}".format(str(uid)))
    if request.method == 'GET':
        data = ["1000.jpg", "1001.jpg", "1002.jpg", "1003.jpg", "1004.jpg"]
        return Response(data)