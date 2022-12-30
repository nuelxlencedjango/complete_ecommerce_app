from django.urls import path
from .views import *
from .import views
#from loginApp import views


app_name = 'products'
urlpatterns = [
    path('', views.indexPage, name='home'),
     path('collection', views.category, name='collection'),
    path('categoryitems/<str:slug>', views.categoryProducts, name='categoryitems'),
    path('categoryitems/<str:cate_slug>/<str:product_slug>/', views.productDetail, name='product_detail'),

    path('add_to_cart',views.addToCart , name='add_to_cart'),
    path('delete_cart_item',views.removeCartItem , name='delete_cart_item'),
    path('cart',views.cartItem , name='cart'),
     path('update_cart',views.updateCartItem , name='update_cart'),
     path('wishes',views.wishList , name='wishes'),
    path('addTowishList',views.WishItems, name='addTowishList'), 
    path('delete_wishlist_item',views.deleteWishListItem, name='delete_wishlist_item'), 
  
]

