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

    path('checkout',views.checkoutItems , name='checkout'),
    path('place_order', views.placeOrder, name='place_order'),
    
    path('payment_confirmed/', views.payment_confirmation, name='payment_confirmed'),
   path('my_orders/', views.myOrders, name='my_orders'),
   
    path('view_orders/<str:tk_no>/', views.myOrdersList, name='view_orders'),

    path('proceed-to-pay/', views.razorpaycheckout, name='proceed-to-pay'),


    path('newL/', views.newLink, name='newL'),
     path('itmD/<int:pk>/', views.itmDetails, name='itmD'),
     path('prod-request/',views.productReq, name="prod-request"),
     path('peoduct_list/', views.productListAjax,name='peoduct_list'),

    path('search-product/', views.productSearch,name='search-product'), 
    
]

