# coding: utf-8

from rest_framework import serializers
from webapps.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('uid', 'date', 'favorites', 'comments', 'regression_error', 'features', 'file_path')