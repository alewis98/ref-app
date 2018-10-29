from django.contrib import admin
from django.contrib.auth.admin import *
from .models import *

models = [Player, Coach, Referee, Division, Team, Game]

for model in models:
    admin.site.register(model)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name','is_admin')

    def name(self, obj):
        return str(obj.user.first_name) + " " + str(obj.user.last_name)

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-is_admin', 'user')
        return queryset

admin.site.register(UserProfile, UserProfileAdmin)