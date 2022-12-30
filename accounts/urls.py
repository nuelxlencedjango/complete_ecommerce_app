from django.urls import path
from .views import *
from .import views
#from loginApp import views


app_name = 'accounts'
urlpatterns = [
    path('registration', views.signUp, name='registration'),
    path('login', views.loginView, name='login'),

    path('logout', views.logoutPage, name='logout'),
  
 
]

