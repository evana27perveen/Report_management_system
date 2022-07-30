from django.contrib import admin
from django.urls import path
from . import views

app_name = 'App_login'

urlpatterns = [
    path('hod-signup/', views.hod_signup, name='hod-signup'),
    path('officer-signup/', views.officer_signup, name='officer-signup'),
    path('reporter-signup/', views.reporter_signup, name='reporter-signup'),
    path('employee-login/', views.hod_officer_login, name='hod-login'),
    path('reporter-login/', views.reporter_login, name='reporter-login'),
    path('logout/', views.logout_system, name='logout'),
]
