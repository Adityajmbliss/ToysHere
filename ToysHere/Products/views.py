from unicodedata import category
from django import views
from django.shortcuts import render
from django.views import View
from Products.models import *

# Create your views here.
def index(request):
    slider = HomepageBanner.objects.all().order_by('-id')
    Homedata = {
        'slider' : slider

    }
    return render(request,'index.html',Homedata)

# category 
def category(request):
    category = Category.objects.all().order_by('-id')
    Catdata = {
        'categories' : category

    }
    return render(request,'categories.html',Catdata)

# brands
def brand(request):
    brand = Brand.objects.all().order_by('name')
    Branddata = {
        'brand' : brand

    }
    return render(request,'brands.html',Branddata)

# my-account 
def myaccount(request):
    return render(request,'my-account.html')

# cart 
def cart(request):
    return render(request,'cart.html')



