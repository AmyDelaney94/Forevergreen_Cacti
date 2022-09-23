''' Loading imports at beginning of file '''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile')
]
