from django.contrib import admin
from django.contrib.auth.admin import *
from .models import *

models = [UserProfile, Player, Coach, Division, Team, Game]

for model in models:
    admin.site.register(model)

