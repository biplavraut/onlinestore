from django.shortcuts import render
from .models import Product, ProductDiscount

def base(request):
 return render(request, 'app/base.html')

def home(request):
    products = Product.objects.all() # Get all products from the DD and store it in 'products' variable.

    return render(request, 'app/home.html', {'products':products})

def product_detail(request):
    return render(request, 'app/productdetail.html')

def add_to_cart(request):
    return render(request, 'app/addtocart.html')

def buy_now(request):
    return render(request, 'app/buynow.html')

def profile(request):
    return render(request, 'app/profile.html')

def address(request):
    return render(request, 'app/address.html')

def orders(request):
    return render(request, 'app/orders.html')

def change_password(request):
    return render(request, 'app/changepassword.html')

def mobile(request):
    return render(request, 'app/mobile.html')

def login(request):
    return render(request, 'app/login.html')

def customerregistration(request):
    return render(request, 'app/customerregistration.html')

def checkout(request):
    return render(request, 'app/checkout.html')
