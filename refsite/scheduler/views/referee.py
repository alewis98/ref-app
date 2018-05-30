from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from scheduler.forms import RegistrationForm, EditProfileForm, RefereeRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from scheduler.models import *

class RefereeView(TemplateView):
    template_name = "referee/register.html"

    def get(self, request):
        form = RefereeRegistrationForm()
        args = {"form": form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = RefereeRegistrationForm(request.POST)
        if form.is_valid():
            # Create Referee
            data = form.cleaned_data
            referee = Referee.objects.create(
                user=request.user.userprofile,
                grade=data['grade'],
                years_experience=data['years_experience'],
                is_certified=data['is_certified']
                )
            referee.save()
            # Set is_referee to True on UserProfile
            profile = request.user.userprofile
            profile.is_referee = True
            profile.save()
            return redirect('/referee')
        else:
            form = RefereeRegistrationForm(user=request.user.userprofile)
            args = {"form": form}
            return render(request, self.template_name, args)