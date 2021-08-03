from django.db import models

# Create your models here.
    
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/product_img/productname.jpg
    
    # upload_to = "product_img"
    upload_to = instance.media_root
    ext = filename.split('.')[-1]
    filename = instance.product_name
    return '{0}/{1}.{2}'.format(upload_to, filename, ext)

def calculate_discount(product_id, list_price):
    current_price = list_price
    product_discount = ProductDiscount.objects.filter(product_id=product_id).last()

    if product_discount:
        discount_rate = product_discount.discount_rate
        discount = current_price * (discount_rate/100)
        return discount
    else:
        return 0 ## Send user a message to set up discount for a product. Do not change the boolean value (On Sale) to True in this scenareio.

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
    media_root = "product_category"
    # media_name = category_title
    def __str__(self):
        return self.category_title

class Brand(models.Model):
    brand_name = models.CharField(max_length = 100)
    brand_tagline= models.CharField(max_length = 200)
    logo = models.ImageField(upload_to = "brand_logo",default='noimg.png', null=True)
    display = models.BooleanField(default=True)
    brand_description= models.TextField(max_length = 200, null= True)
    media_root = "brand_logo"
    def __str__(self):
        return self.brand_name

    # def get_brand_name(self):
    #     return self.brand_name

class Product(models.Model):
    # product_id = primary key will be automatically created when an object is added.
    product_name = models.CharField(max_length = 100)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE, default = None, null = True)
    product_category = models.ForeignKey(ProductCategory, on_delete= models.CASCADE, default = None, null = True)
    release_date = models.DateTimeField("date released")
    img = models.ImageField(upload_to = user_directory_path )
    list_price = models.FloatField(default = None, blank = True, null = True)
    discount = models.FloatField(default=0)
    on_sale = models.BooleanField(default=False)
    product_description= models.TextField(max_length = 200)
    media_root = "product_img"
    # media_name = product_name
    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        if self.on_sale:
            self.discount = calculate_discount(self.id, self.list_price)
        elif not self.on_sale:
            self.discount = 0
        super(Product, self).save(*args, **kwargs) 


class ProductDiscount(models.Model):
    product_id = models.ForeignKey(Product, on_delete= models.CASCADE)
    discount_rate = models.FloatField(default=0)

    def __str__(self):
        return str(self.product_id)

    def get_discount_rate(self, *args, **kwargs):
        return self.discount_rate
    
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

gender_options = (('M',"Male"),(
'F', "Female"))
class Contact(models.Model):
    gender = models.CharField(choices=gender_options, max_length = 50, null= True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number= models.CharField(max_length=255, default=None, null = False)
    message = models.TextField(null= True)

    def __str__(self):
        return  self.name

