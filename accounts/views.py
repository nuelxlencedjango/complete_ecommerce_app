
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from .forms import *
from django.http.response import JsonResponse
from .models import *
from products.forms import *
from products .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




def signUp(request):
    form = CreateUserForm()
    form2 = CustomerDetailsForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form2 = CustomerDetailsForm(request.POST)
       
        if form.is_valid() and form2.is_valid():
            user = form.save()
            #associate detail information to the user before saving
            profile = form2.save(commit=False)
            profile.user =user
            profile.save()

            messages.success(request, 'Account successfully created ' )

            return redirect('accounts:login')

        else:
            form =CreateUserForm(request.POST)
            form2 = CustomerDetailsForm(request.POST)
            messages.success(request,"account was not created")  
            context = {'form':form, 'form2': form2}  
            return render(request, 'accounts/register.html', context)


   # messages.success(request, 'heelo,welcome!')    
    context = {'form':form, 'form2': form2}   
    return render(request, 'accounts/register.html', context)    
            

          



def loginView(request):
    if request.user.is_authenticated:
        messages.success(request,"You are login already") 
        return redirect('products:home')

    else:    
        form = UserLoginForm()
        if request.method == 'POST':
            form = UserLoginForm(data=request.POST)
       
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user=authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('products:home')

            return render(request, 'accounts/login.html', context={'form': form, 'error': 'Invalid username or password'})
      
        context={'form':form}
        return render(request, 'accounts/login.html', context)
      



@login_required
def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"You logged out successfully.") 
        return redirect('products:home')


