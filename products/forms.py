from datetime import date
from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.widgets import DateInput


from .models import *





class OrderForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()
    address = forms.Textarea()
    city = forms.CharField()
    state = forms.CharField()
    pin_code = forms.CharField()
    country = forms.CharField()
    total_price = forms.FloatField()
    payment_mode = forms.CharField()
  
    

    class Meta:
        model = Order
        fields =('first_name','last_name','email','phone','address', 'city','state','pin_code','country',
                 'total_price','payment_mode') 

        Widget ={
          
            'first_name':forms.TextInput( attrs={'class':'form-control','placeholder':'First Name'}),
            
            'last_name':forms.TextInput( attrs={'class':'form-control'}),
            'email':   forms.TextInput( attrs={'class':'form-control'}),
        
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'address':   forms.TextInput( attrs={'class':'form-control'}),
            'city':   forms.TextInput( attrs={'class':'form-control'}),
            'state':forms.TextInput( attrs={'class':'form-control'}),
            'pin_code':   forms.TextInput( attrs={'class':'form-control'}),
            'country':   forms.TextInput( attrs={'class':'form-control'}),
            'total_price':   forms.TextInput( attrs={'class':'form-control'}),
            'payment_mode':   forms.TextInput( attrs={'class':'form-control'}),
           
            }
            