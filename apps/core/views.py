from django.shortcuts import render

from apps.store import models

def frontpage(request):
    products = models.Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'frontpage.html', context)


def contact(request):
    return render(request, 'contact.html')
