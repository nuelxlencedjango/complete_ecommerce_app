from django.contrib.auth.models import AbstractUser

from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User
from django.urls import reverse
from .models import *

from django_countries.fields import CountryField
from cloudinary.models import CloudinaryField





class CustomerDetails(models.Model):
    user = models.OneToOneField(User, on_delete= models.SET_NULL,related_name='customer',null=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    dateRegistered =models.DateTimeField(auto_now_add=True, null=True)
    country = CountryField(blank=True)
    phone = models.CharField(max_length=50,null=True)
   # profile_img = CloudinaryField(blank=True,null=True)
   
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural='Customer Details'


    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if self.dateRegistered is None:
            self.dateRegistered = timezone.localtime(timezone.now())

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.uniqueId = slugify('{} {}'.format(self.user, self.uniqueId))

      
        self.last_updated = timezone.localtime(timezone.now())

        super(CustomerDetails, self).save(*args, **kwargs)       