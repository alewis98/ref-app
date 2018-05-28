from django.shortcuts import render, HttpResponse

from . import account

def home(request):
    return render(request, 'home.html')

