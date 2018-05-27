from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),
]