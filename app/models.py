from django.db import models

# Create your models here.
Shop_Sections = (
    ('Electronics', 'Electronics'),
    ('Fashion', 'Fashion'),
    ('Grocery', 'Grocery')
)
class ProductCategory(models.Model):
    category_title = models.CharField(max_length = 100)
    shop_section = models.CharField(choices=Shop_Sections, max_length = 50)
    img = models.ImageField(upload_to = "product_category", default='noimg.png', null=True)
    display = models.BooleanField(default=True)
    category_description= models.TextField(max_length = 200, null= True)
    def __str__(self):
        return self.category_title

class Brand(models.Model):
    brand_name = models.CharField(max_length = 100)
    brand_tagline= models.CharField(max_length = 200)
    logo = models.ImageField(upload_to = "brand_logo",default='noimg.png', null=True)
    display = models.BooleanField(default=True)
    brand_description= models.TextField(max_length = 200, null= True)
    def __str__(self):
        return self.brand_name

class Product(models.Model):
    # product_id = primary key will be automatically created when an object is added.
    product_name = models.CharField(max_length = 100)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE, default = None, null = True)
    product_category = models.ForeignKey(ProductCategory, on_delete= models.CASCADE, default = None, null = True)
    release_date = models.DateTimeField("date released")
    img = models.ImageField(upload_to = "product_img")
    list_price = models.FloatField(default = None, blank = True, null = True)
    discount = models.FloatField(default=0, blank=False, null=  False)
    on_sale = models.BooleanField(default=False)
    product_description= models.TextField(max_length = 200)
    def __str__(self):
        return self.product_name

    def calculate_discount(self):
        return 0

class ProductDiscount(models.Model):
    product_id = models.ForeignKey(Product, on_delete= models.CASCADE)
    discount_rate = models.FloatField(default=0)
    
class LatestBlog(models.Model):
    blog_name = models.CharField(max_length=100)
    blog_description = models.TextField()
    release_date = models.DateTimeField("date released")
    img = models.ImageField(upload_to = "blog_img")

    def __str__(self):
        return self.blog_name

class Slider(models.Model):
    title = models.CharField(max_length = 255)
    sub_title = models.CharField(max_length = 255)
    img = models.ImageField(upload_to ="slider_img")
    display = models.BooleanField(default = False)
    link = models.CharField(max_length = 255)
    slider_description = models.TextField(max_length=200)


    def __str__(self):
        return self.title
