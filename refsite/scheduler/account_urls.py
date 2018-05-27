from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    # Accounts
    path('signup/referee', views.referee.signup, name='referee-signup'),
    path('login/', login, {'template_name': 'accounts/login.html'}),
    path('logout/', logout, {'template_name': 'accounts/logout.html'}),
    path('profile/', views.referee.profile, name='profile'),
]