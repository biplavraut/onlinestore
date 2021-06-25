from django.contrib import admin
from .models import ProductCategory, Brand ,Product, ProductDiscount, LatestBlog, Slider

# Register your models here.
admin.site.register(LatestBlog)
@admin.register(ProductCategory)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_title', 'shop_section','img','display','category_description']


admin.site.register(Brand)
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'brand', 'product_category', 'list_price','discount','on_sale','img','release_date']

admin.site.register(ProductDiscount)
admin.site.register(Slider)