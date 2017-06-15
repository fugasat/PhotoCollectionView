from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters
from .serializer import PhotoSerializer
from webapps.models import Photo


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
