from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.homepage, name='home_page'),
     path('about', views.aboutpage, name='about_bage'),
]