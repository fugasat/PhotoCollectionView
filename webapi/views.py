from django.shortcuts import render
import django_filters
from django.http import Http404
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


def response_relation(relation):
    if relation is None:
        raise Http404

    uids = relation["uids"][:30]
    datas = Photo.objects.filter(uid__in=uids).values()
    # 正しい順番でソート
    data = []
    for s_uid in uids:
        for item in datas:
            if item["uid"] == s_uid:
                data.append(item)
    result = {}
    result["info"] = ",".join(relation["info"])
    result["relation"] = data
    result["similarity"] = relation["similarity"][:30]
    result["type_similarity"] = relation["type_similarity"]
    return Response(result)


@api_view(['GET'])
def get_relation(request, pre_uid, uid, relation_type=None):
    uid = int(uid)
    if request.method == 'GET':
        # 類似度が高いデータを6個取得
        relation = __features.get_relation_uids(pre_uid, uid, relation_type)
        return response_relation(relation)


@api_view(['GET'])
def get_relation_from_history(request, uid, history):
    if request.method == 'GET':
        uids = history.split("x")
        relation = __features.get_relation_uids_from_history(uids)
        return response_relation(relation)
