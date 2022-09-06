''' Adding imports to beginning of file '''
from django.urls import path
from .import views

urlpatterns = [
    path('', views.add_subscriber, name='newsletter'),
]
