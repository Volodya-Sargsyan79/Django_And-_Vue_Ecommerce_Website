from django.urls import path

from .api import api_add_to_cart, api_remove_from_cart

urlpatterns = [
    path('add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),
]
