from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Photo
from webapps.const import Const


def index(request):
    photo_list = Photo.objects.order_by('-uid')
    context = {'photo_list': photo_list}
    return render(request, 'index.html', context)


def detail(request, uid):
    try:
        photo = Photo.objects.get(uid=uid)
    except Photo.DoesNotExist:
        raise Http404("Photo does not exist")
    return render(request, 'detail.html', {'photo': photo})


def relation(request, uid, relation_type=Const.type_total()):
    try:
        photo = Photo.objects.get(uid=uid)
    except Photo.DoesNotExist:
        raise Http404("Photo does not exist")
    return render(request, 'relation.html', {'photo': photo, 'relation_type': relation_type})
