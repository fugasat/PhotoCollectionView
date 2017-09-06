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


def response_relation(relations):
    if relations is None:
        raise Http404

    result = {}
    for key in relations.keys():
        relation = relations[key]

        uids = relation["uids"][:30]
        datas = Photo.objects.filter(uid__in=uids).values()
        data = []
        for s_uid in uids:
            for item in datas:
                if item["uid"] == s_uid:
                    data.append(item)

        info = None
        if relation["info"] is not None:
            info = ",".join(relation["info"])

        result[key] = {
            "info": info,
            "relation": data,
            "similarity": relation["similarity"][:30],
            "type_similarity": relation["type_similarity"]
        }
    return Response(result)


@api_view(['GET'])
def get_relation(request, uid, relation_type=None, history=None):
    uid = int(uid)
    if request.method == 'GET':
        uids = history.split("x")
        relations = __features.get_relation(uid, uids)
        return response_relation(relations)
