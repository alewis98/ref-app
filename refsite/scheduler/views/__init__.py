from django.shortcuts import render, HttpResponse

from . import referee

def home(request):
    return HttpResponse("hi")

