from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World! You are at the Photo Collection View index.")