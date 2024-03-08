from django.urls import path

from .views import frontpage, contact
from apps.store.views import product_detail, category_detail

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('contact/', contact, name='contact'),
    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:slug>/', category_detail, name='category_detail'),
]
