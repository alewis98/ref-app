from django.urls import path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),
    # Accounts
    path('signup/referee', views.referee.signup, name='referee-signup'),
    path('login', login, {'template_name': 'accounts/login.html'}),
]