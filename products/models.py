from django.db import models
import datetime
from django.contrib.auth.models import User
import os

# Create your models here.

def get_file_path(request, filename):
    original_filename =filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime,original_filename)
    return os.path.join('upload/', filename)


class Category(models.Model):
    slug = models.CharField(max_length=100,null=False,blank=False)
    name = models.CharField(max_length=100,null=False,blank=False)
    productImg = models.ImageField(upload_to=get_file_path, null=True,blank=True)
    description = models.TextField(max_length=500,null=True,blank=True)
    status = models.BooleanField(default=False,help_text="0-default, 1-Hidden")
    trending = models.BooleanField(default=False,help_text="0-default, 1-Hidden")
    meta_title = models.CharField(max_length=100,null=False,blank=False)
    meta_keywards = models.CharField(max_length=100,null=False,blank=False)
    meta_description = models.TextField(max_length=500,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=100,null=False,blank=False)
    name = models.CharField(max_length=100,null=False,blank=False)
    img = models.ImageField(upload_to=get_file_path, null=True,blank=True)
    description = models.TextField(max_length=500,null=True,blank=True)
    small_description = models.CharField(max_length=500,null=True,blank=True)
    status = models.BooleanField(default=False,help_text="0-default, 1-Hidden")
    trending = models.BooleanField(default=False,help_text="0-default, 1-Hidden")
    tag = models.CharField(max_length=100,null=True,blank=True)
    original_price =models.FloatField(blank=False, null=False)
    selling_price =models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    meta_title = models.CharField(max_length=100,null=False,blank=False)
    meta_keywards = models.CharField(max_length=100,null=False,blank=False)
    meta_description = models.TextField(max_length=500,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)



    def __str__(self):
        return self.name





class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(default=1, blank=False)
   # uniPrice= models.IntegerField(default=1, blank=False)
    #totalPrice = models.IntegerField(default=1, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
   
  
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural='Cart'

   



class WishList(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #product_qty = models.IntegerField(default=1, blank=False)
   # uniPrice= models.IntegerField(default=1, blank=False)
    #totalPrice = models.IntegerField(default=1, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
   
  
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural='Wishlist'

