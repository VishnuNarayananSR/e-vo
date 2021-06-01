from os import name
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'voters'

urlpatterns = [
    # path('', views.voter_home),
    path('register/', views.voter_registration, name='register'),
    path('vote/', views.vote, name='vote'),
]
