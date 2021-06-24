from django.contrib import admin
from .models import Product, ProductDiscount, LatestBlog

# Register your models here.
admin.site.register(LatestBlog)
admin.site.register(Product)
admin.site.register(ProductDiscount)