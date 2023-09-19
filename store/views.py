from django.shortcuts import render, get_object_or_404
# Create your views here.

from django.shortcuts import redirect

from .models import Category, Product

def all_products(request):
    products = Product.products.all()
    return render(request, 'store/index.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_stock=True)
    return render(request, 'store/products/single.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})
