from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("You are at the scheduler index.")