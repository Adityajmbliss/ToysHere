from unicodedata import category
from django import views
from django.shortcuts import render
from django.views import View
from Products.models import *

# Create your views here.
def index(request):
    slider = HomepageBanner.objects.all().order_by('-id')
    brands = Brand.objects.all()[0:4]
    categories = Category.objects.all()[0:3]
    Products  = Product.objects.all()[0:3]
    Homedata = {
        'slider' : slider,
        'brand' : brands,
        'category' : categories,
        'products' : Products

    }
    return render(request,'index.html',Homedata)

# category 
def category(request):
    category = Category.objects.all().order_by('Cat_Name')
    Catdata = {
        'categories' : category

    }
    return render(request,'categories.html',Catdata)

# brands
def brand(request):
    branddata = Brand.objects.all().order_by('id')
    Branddata = {
        'brand' : branddata

    }
    return render(request,'brand.html',Branddata)

# my-account 
def myaccount(request):
    return render(request,'my-account.html')

# cart 
def cart(request):
    return render(request,'cart.html')



