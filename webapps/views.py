from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Photo



def index(request):
    photo_list = Photo.objects.order_by('uid')
    context = {'photo_list': photo_list}
    return render(request, 'index.html', context)


def detail(request, photo_uid):
    try:
        photo = Photo.objects.get(uid=photo_uid)
    except Photo.DoesNotExist:
        raise Http404("Photo does not exist")
    return render(request, 'detail.html', {'photo': photo})
