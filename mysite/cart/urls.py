from django.urls import path
from .views import *

urlpatterns = [
path('cart/', CartView.as_view()),
path('cart/items/', CartItemViewSet.as_view({'get': 'list','post': 'create'})),
path('cart/items/<int:pk>/', CartItemViewSet.as_view({'put': 'update','delete': 'destroy'})),
]