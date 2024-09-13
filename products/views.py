from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product , Category
from django.utils import timezone
from .models import Product, Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', context= {'products':products , 'title' : "All Products"})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html',{'product': product})

def product_recent(request):
    time_day_ago = timezone.now() - timezone.timedelta(days=1)
    recent_products = Product.objects.filter(created_at__gte=time_day_ago)
    return render(request, 'products/most_recent.html', {'recent_products' : recent_products})


def get_category(request, category_name):
    category_product = Category.objects.filter(name=category_name).first()

    return render(request, 'products/product_list.html',
                  context={"products": category_product.products.all(), "title": f"{category_name} Products".capitalize()})


@login_required
def order_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.user = request.user
            order.status = 'received'  
            if product.stock > 0:
                product.stock -= 1
                product.save()
                order.save()
                return redirect('profile')  
    else:
        form = OrderForm(initial={
            'name': request.user.get_full_name(),
            'email': request.user.email,
            'phone': getattr(request.user, 'phone', ''),  
        })
    
    return render(request, 'products/order_form.html', {'form': form, 'product': product})


def order_success(request):
    return render(request, 'products/order_success.html')