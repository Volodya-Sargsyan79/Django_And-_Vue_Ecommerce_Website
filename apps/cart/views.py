from django.shortcuts import render

from .cart import Cart

def cart_detail(request):
    cart = Cart(request)
    productsstring = ''

    for item in cart:
        product = item['product']
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total_price'])

        productsstring = productsstring + b

    print(cart.get_total_length(), 22222)

    context = {
        'cart': cart,
        'productsstring': productsstring,
        'prquantity': cart.get_total_length()
    }

    return render(request, 'cart.html', context)
