from django.contrib import admin
from .models import Product, ProductDiscount, LatestBlog, Slider

# Register your models here.
admin.site.register(LatestBlog)
admin.site.register(Product)
admin.site.register(ProductDiscount)
admin.site.register(Slider)