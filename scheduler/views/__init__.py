from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from scheduler.forms import RegistrationForm, EditProfileForm, RefereeRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from scheduler.models import *

from . import account, referee

def home(request):
    return render(request, 'home.html')

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        games = Game.objects.all()
        args = {
            "games": games
        }
        return render(request, self.template_name, args)