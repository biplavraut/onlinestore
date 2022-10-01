from django.contrib import admin
from .models import Players, ProductCategory, Brand ,Product, ProductDiscount, LatestBlog, Slider, Contact

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
admin.site.register(Contact)

@admin.register(Players)
class PlayersModelAdmin(admin.ModelAdmin):
    list_display= ['name', 'type', 'room']
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False