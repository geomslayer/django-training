from django.shortcuts import render
from .models import Product


def main_page(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})
