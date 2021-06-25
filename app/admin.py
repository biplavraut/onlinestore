from django.contrib import admin
from .models import Product, ProductDiscount, LatestBlog, Slider

# Register your models here.
admin.site.register(LatestBlog)

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'list_price','discount','on_sale','img','release_date']

admin.site.register(ProductDiscount)
admin.site.register(Slider)