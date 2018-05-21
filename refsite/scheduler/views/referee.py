from django.shortcuts import render, HttpResponse

def signup(request):
    return render(request, 'accounts/referee_signup.html')