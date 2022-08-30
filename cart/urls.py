'''Added imports to beggining of file'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<item_id>/', views.update_cart, name='update_cart'),
    path('delete/<item_id>/', views.delete_cart, name='delete_from_cart'),
]
