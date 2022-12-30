from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import *



class CreateUserForm(UserCreationForm):
    username =forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Your username'}))
    first_name =forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Your First name'}))
    last_name =forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Your Last name'}))
    email =forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Your email'}))
    password1 =forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Your password'}))
    password2 =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'confirm password'}))
    class Meta:
        model = User
       
        fields = ('username', 'email', 'password1', 'password2','first_name','last_name')




class CustomerDetailsForm(forms.ModelForm):
    phone =forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Your Phone number'}))
    #country =forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Your First name'}))
    nationality = CountryField()
    class Meta:
        model = CustomerDetails
       
        fields = ('phone', 'country')
    
    def __init__(self,*args, **kwargs):
        super(CustomerDetailsForm, self).__init__(*args,**kwargs)

        self.fields['country'].empty_label = "Select country"





class UserLoginForm(AuthenticationForm):
    username =forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Your username'}))
    password =forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Your password'}))
   
    class Meta:
        model = User
       
        fields = ('username', 'password')

    
