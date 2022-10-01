from datetime import datetime
from re import I
from xml.etree.ElementTree import tostring
from django.contrib.admin.decorators import display
from django.shortcuts import render
from .models import Players, Product, ProductDiscount, LatestBlog, Slider, Brand, ProductCategory, Contact
from django.http import HttpResponse, JsonResponse

def base(request):
 return render(request, 'app/base.html')

def home(request):
    products = Product.objects.all() # Get all products from the DD and store it in 'products' variable.
    blogs = LatestBlog.objects.all()
    sliders = Slider.objects.all()
    brands = Brand.objects.filter(display=True)
    product_categories = ProductCategory.objects.all()
    contacts = Contact.objects.all()
     

    return render(request, 'app/home.html', {'brands':brands,'product_categories': product_categories, 'products':products, 'blogs':blogs, 'sliders123':sliders, 'contacts':contacts})

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


def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        message = request.POST.get('comment')
        contact.name = name
        contact.email = email
        contact.phone_number = phone_number
        contact.message = message
        saveContact = contact.save()
        # Return to html file
        if saveContact:
            return render(request, 'app/contact.html', {'message':'message-sent'})
        else:
            return render(request, 'app/contact.html', {'message':'message-error'})
        
    return render(request, 'app/contact.html')

def loading(request):
    return render(request, 'app/loading.html')


def player(request):

    if request.method == "POST":
        randomRoom= "ROOM-"+ datetime.now().strftime("%H%M%S%f")
       
        for i in range(1,5):
            if i == 1: pname = "pname1"
            elif i==2: pname= "pname2"
            elif i==3: pname= "pname3"
            else : pname= "pname4"
            player = Players()
            room= randomRoom

            name= request.POST.get(pname)
            type= i
            player.name=name
            player.type= type
            player.room=room
            savePlayer = player.save()
        if savePlayer: 
            
        
            return render(request, 'app/game.html', {'message': player})

    

    return render(request, 'app/players.html')