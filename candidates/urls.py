from django.contrib import admin
from django.urls import path
from . import views

app_name = 'candidates'

urlpatterns = [
    path('register', views.register, name='register'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('start_election/', views.start_election, name='start_election'),
    path('end_election/', views.end_election, name='end_election'),
]
