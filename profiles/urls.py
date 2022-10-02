''' Loading imports at beginning of file '''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    # Wish List
    path('wishlist/', views.wishlist,
         name="view_wishlist"),

    path('wishlist/add_to_wishlist/<int:id>',
         views.add_to_wishlist, name="wishlist"),
]
