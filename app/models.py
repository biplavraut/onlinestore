from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length = 100)
    product_description= models.CharField(max_length = 200)
    release_date = models.DateTimeField("date released")
    img = models.ImageField(upload_to = "images")
    list_price = models.FloatField(default = None, blank = True, null = True)
    discount = models.FloatField(default=0, blank=False, null=  False)

class ProductDiscount(models.Model):
    product_id = models.ForeignKey(Product, on_delete= models.CASCADE)
    discount_rate = models.FloatField(default=0)
    