from django.urls import path
#from django.contrib.auth.views import login, logout
from .views import *

app_name = 'home'
urlpatterns = [
    # Homepage
    path('', HomeView.as_view(), name='home'),
]