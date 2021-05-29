from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.voter_home),
    path('register/', views.voter_registration),

]
