
from django.contrib import admin

from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User



admin.site.register(CustomerDetails)


