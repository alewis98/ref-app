from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db import transaction
from scheduler.models import *
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return User

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )

class EditUserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ['image', 'phone_number', 'address', 'date_of_birth']

class RefereeRegistrationForm(ModelForm):

    class Meta:
        model = Referee
        fields = ['grade', 'years_experience', 'is_certified']