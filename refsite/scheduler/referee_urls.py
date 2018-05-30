from django.urls import path, re_path
from django.conf.urls import url
from .views.referee import *


app_name = 'referee'
urlpatterns = [
    path('register/', RefereeView.as_view(), name='register'),
]