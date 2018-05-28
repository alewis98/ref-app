from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    # Accounts
    path('signup/referee', views.referee.signup, name='referee-signup'),
    path('login/', login, {'template_name': 'accounts/login.html'}),
    path('logout/', logout, {'template_name': 'accounts/logout.html'}),
    path('profile/', views.referee.view_profile, name='view-profile'),
    path('profile/edit/', views.referee.edit_profile, name='edit-profile'),
    path('change_password/', views.referee.change_password, name='change-password'),
    path('reset_password/', password_reset, name='reset-password'),
    path('reset_password/done/', password_reset_done, name='password_reset_done'),
#    path('reset_password/confirm/<uuid:uidb64>/', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    path('reset_password/complete/', password_reset_complete, name='password_reset_complete'),

]