from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from scheduler.forms import RegistrationForm
from django.contrib.auth.models import User

# def signup(request):
#     return render(request, 'accounts/referee_signup.html')

def signup(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/referee_signup.html', args)

def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)
