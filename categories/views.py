from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Category
from products.models import Product
# Create your views here.

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories' : categories})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'category_products.html', {
        'category': category,
        'products': products
    })