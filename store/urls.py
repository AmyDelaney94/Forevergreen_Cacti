""" Loading imports at beggining of file"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='store'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy')
]
