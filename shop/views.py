from django.shortcuts import render
from .models import Product


def products_page(request):
    products = Product.objects.order_by('order', 'name').all()
    return render(request, 'shop/product_list.html', {'products': products})


def contacts_page(request):
    return render(request, 'shop/contacts.html')
