''' Adding Imports to beggining of file '''
from django.urls import path
from .views import (
    ReviewDeleteView,
    ReviewUpdateView,
)
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path(
        'reviews/<int:pk>/update/',
        ReviewUpdateView.as_view(),
        name='review-update'
        ),
    path(
        'reviews/<int:pk>/delete/',
        ReviewDeleteView.as_view(),
        name='review-delete'
        ),
    path('<product_id>', views.product_detail, name='product_detail'),
]
