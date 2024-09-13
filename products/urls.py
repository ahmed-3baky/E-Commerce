from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('product_recent', views.product_recent, name='product_recent'),
    path('categories/<str:category_name>', views.get_category, name='category'),
    path('order/<int:product_id>/', views.order_product, name='order_product'),  
    path('order/success/', views.order_success, name='order_success'),


]