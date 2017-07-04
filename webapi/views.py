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
def get_relation(request, uid, relation_type=None):
    uid = int(uid)
    if request.method == 'GET':
        # 類似度が高いデータを6個取得
        uids = __features.get_relation_uids(uid, relation_type)[:10]
        datas = Photo.objects.filter(uid__in=uids).values()
        # 正しい順番でソート
        data = []
        for s_uid in uids:
            for item in datas:
                if item["uid"] == s_uid:
                    data.append(item)
        return Response(data)
