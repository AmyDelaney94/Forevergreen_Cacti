''' Adding Imports to beggining of file '''
from django.urls import path
from .views import (
    DeleteReview,
    UpdateReview,
)
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path(
        'reviews/<int:pk>/update/',
        UpdateReview.as_view(),
        name='review-update'
        ),
    path(
        'reviews/<int:pk>/delete/',
        DeleteReview.as_view(),
        name='DeleteReview'
        ),
    path('<product_id>', views.product_detail, name='product_detail'),
]
