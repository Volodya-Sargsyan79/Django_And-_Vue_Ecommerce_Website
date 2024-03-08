from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from cart.cart import Cart

from .models import Product

def api_add_to_cart(request):
    jsonresponse = {'success': True}
    product_id = request.POST.get('product_id')
    update = request.POST.get('update')

    cart = Cart(request)

    product = get_object_or_404(Product, pk=product_id)