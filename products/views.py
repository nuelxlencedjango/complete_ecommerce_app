from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.http.response import JsonResponse
from accounts .models import *
from django.contrib import  messages
from django.contrib.auth.decorators import login_required
import random
from .forms import *


def indexPage(request):
    trending =Product.objects.filter(trending=1)
   # trending =Product.objects.filter(trending=0)
    context={'trending':trending}
    return render (request, 'shop/index.html',context)



def category(request):
    cate = Category.objects.filter(status=0)
    context ={'category':cate}
    return render (request, 'shop/category.html',context)



def categoryProducts(request,slug):
    if Category.objects.filter(slug = slug).exists():
        products = Product.objects.filter(category__slug =slug) #accessing category slugs
        category_name =Category.objects.filter(slug=slug).first()
        context ={'products':products,'category_name':category_name}

        return render(request,'shop/products.html',context)
    
    else:
        messages.warning(request, 'No category of such found')
        return redirect('products:collection')






def productDetail(request, cate_slug, product_slug):
    if Category.objects.filter(slug=cate_slug, status=0):
        if Product.objects.filter(slug=product_slug,status=0):
            item = Product.objects.filter(slug=product_slug, status=0).first()
            context={'product':item}
            
        else:
           messages.warning(request,"no such item found")  
           return redirect('products:collection')   
    
    else:
        messages.warning(request,"no such item found")
        return redirect('products:home')

    return render(request,'shop/productDetail.html',context)    




def addToCart(request):
    if request.method =="POST":
        if request.user.is_authenticated:
            prod_id =int(request.POST.get('product_id'))
            productCheck = Product.objects.get(id=prod_id)
            print('productCheck:',productCheck)
            if productCheck:
                if Cart.objects.filter(user =request.user.id, product_id =prod_id):
                    return JsonResponse({'status':'Product already exists'})

                else:
                    prod_qty =int(request.POST.get('product_qty'))
                    print('no,it doest exist there')

                    if productCheck.quantity >= prod_qty:
                        Cart.objects.create(user=request.user,product_id =prod_id, product_qty=prod_qty)
                        return JsonResponse({'status':'successfully added'}) 

                    else:
                        return JsonResponse({'status': "Only" +str(productCheck.quantity) + 'quantity available'}) 

            else:
                return JsonResponse({'status':'No such product available'}) 

        else:
            return JsonResponse({'status':'Login to continue'}) 

    else:
        return redirect('/')                 


                                       
@login_required(login_url='accounts/login')
def cartItem(request):
    if request.user:
        cart = Cart.objects.filter(user=request.user)
        count = len(cart)
    else:
        pass 
    context={'cart':cart,'count':count}
    return render(request, 'shop/cart.html',context)



@login_required(login_url='accounts/login')
def updateCartItem(request):
    if request.method =="POST":
        prod_id =int(request.POST.get('product_id'))
        if Cart.objects.filter(user=request.user,product_id =prod_id):
            prod_qty =int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id =prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()

            messages.warning(request,"successfully updated")
            return JsonResponse({'status':'Successful'}) 
     
    
    return redirect('/')



@login_required(login_url='accounts/login')
def removeCartItem(request):
    if request.method =="POST":
        prod_id =int(request.POST.get('product_id'))
        if Cart.objects.filter(user=request.user,product_id =prod_id):
            cartitem = Cart.objects.get(user=request.user,product_id =prod_id)
            cartitem.delete()
            return JsonResponse({'status':'Item Successful deleted'}) 
    return redirect('/')    


@login_required(login_url='accounts/login')
def wishList(request):
    wish = WishList.objects.filter(user =request.user)
    context={"wish":wish}
    return render(request,"shop/wishlist.html",context) 



@login_required(login_url='accounts/login')
def WishItems(request):
    if request.method =="POST":
        if request.user.is_authenticated:
            prod_id =int(request.POST.get('product_id'))
            productCheck = Product.objects.get(id=prod_id)
            if productCheck:
                if WishList.objects.filter(user =request.user, product_id =prod_id):
                    return JsonResponse({'status':'Product already in wishlist'}) 

                else:
                    WishList.objects.create(user=request.user, product_id =prod_id)   
                    return JsonResponse({'status':'Product added successfully'}) 
            else: 
                return JsonResponse({'status':'No such product found'})  
        else:
            return JsonResponse({'status':'Login to continue'})              
    
    return redirect('products:home')






@login_required(login_url='accounts/login')
def deleteWishListItem(request):
    if request.method =="POST":
        if request.user.is_authenticated:
            prod_id =int(request.POST.get('product_id'))
            if WishList.objects.filter(user =request.user, product_id =prod_id):
                wishlistitem = WishList.objects.get(product_id =prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':'Product already in wishlist'}) 

            else:
                return JsonResponse({'status':'Product not found'}) 

        else:
            return JsonResponse({'status':'Login to continue'})  
                       
    return redirect('products:home')



@login_required(login_url='accounts:login')
def checkoutItems(request):
    rawcart = Cart.objects.filter(user=request.user)

    #checking if quantity in the cart is greater than the available quantity
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id = item.id)


    cartItems =Cart.objects.filter(user = request.user)
    #item price and total price
    total_price =0
    for item in cartItems:
        total_price = total_price + item.product.selling_price * item.product_qty   

    context={"cartItems":cartItems,"total_price":total_price}
    return render(request,'shop/cartItems.html', context)
    #return render(request,'shop/checkout.html', context)



@login_required(login_url='accounts:login')
def placeOrder(request):
    if request.method == "POST":
        order = Order()
        order.user = request.user
        order.first_name = request.POST.get('first_name')
        order.last_name = request.POST.get('last_name')
        order.email = request.POST.get('email')
        order.phone = request.POST.get('phone')
        order.address = request.POST.get('address')
        order.city = request.POST.get('city')
        order.state = request.POST.get('state')
        order.country = request.POST.get('country')
        order.pin_code = request.POST.get('pin_code')
        order.payment_mode = request.POST.get('payment_mode')
        
        #total cart price
        cart = Cart.objects.filter(user = request.user)
        cart_total_price = 0 
        for item in cart:
            cart_total_price += item.product.selling_price * item.product_qty

        order.total_price = cart_total_price  

        #tracking no
        track_no ='nuelMobiles'+str(random.randint(1111111,9999999))  
        while Order.objects.filter(tracking_no=track_no) is None:
            track_no ='nuelMobiles'+str(random.randint(1111111,9999999))

        order.tracking_no =track_no

        order.save()   

        #orderitem products
        order_item_products = Cart.objects.filter(user = request.user)
        for item in order_item_products:
            OrderItem.objects.create(user=request.user, order = order, product=item.product, price =item.product.selling_price, 
                                     quantity =item.product_qty) 
            
            # reducing product quantity from available stock
            order_product =Product.objects.filter(id =item.product.id).first() 
            order_product.quantity = order_product.quantity -item.product_qty
            order_product.save()

        #to clear cart items

        #Cart.objects.filter(user=request.user).delete()
        
        

        if request.POST.get('payment_mode') == "online_payment":
            context ={ 'cart_total_price':cart_total_price}
            return render(request,'shop/card_payment.html',context)
        
        messages.info(request,"Order placed.Shippment on the way.Please get your cash ready.")
        Cart.objects.filter(user=request.user).delete()
        return redirect('/')





@login_required(login_url='accounts:login')
def razorpaycheckout(request):
    cart = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cart:
        total_price += item.product.selling_price * item.product_qty

    return JsonResponse({
        'total_price':total_price
    })    



             

def payment_confirmation(request):
    user = request.user
    
    #if Order.objects.filter(user=request.user, ordered =True).exists():

    messages.info(request,"Your order was successfully placed")
    return render(request,'payments/success.html')



def myOrders(request):
    if Order.objects.filter(user=request.user).exists():
        paid_orders =Order.objects.filter(user=request.user)
        context ={'paid_orders':paid_orders}
    #messages.info(request,"Your order was successfully placed")
    return render(request,'shop/myorders.html', context)



def myOrdersList(request,tk_no):
   order = Order.objects.filter(tracking_no=tk_no).filter(user=request.user).first()
   orderitems = OrderItem.objects.filter(order=order)
   context={'order':order,'orderitems':orderitems}
   return render(request,'shop/order_list.html', context)



def newLink(request):
    items =ProductItems.objects.all()
    context={'items':items}
    return render(request,'shop/newlink.html', context)



   
def itmDetails(request,pk):
    item =ProductItems.objects.get(id=pk)
    context={'item':item}
    return render(request,'shop/itmdetail.html', context)



def productReq(request):
    if request.user.is_authenticated:

        item = request.POST.get('product_name')
        price = request.POST.get('price')
       
        if request.method == "POST":
            Ordered.objects.create(user=request.user,product_name=item, price=price )
            messages.info(request,"your order was successfully ")    
            return redirect('/')
        
    messages.info(request,"please login to make order ")    
    return redirect('/')
    

def productListAjax(request):
    products = Product.objects.filter(status=0).values_list('name',flat=True)
    productslist =list(products)

    return JsonResponse(productslist,safe=False)



def productSearch(request):
    if request.method =="POST":
        items = request.POST.get('search-items')
        if items == "":
            #previous page
            return redirect(request.META.get("HTTP_REFERER"))
            
        
        else:
            product = Product.objects.filter(name__contains=items).filter()

            if product:
                #return redirect("collections/"+product.category.slug+'/'+product.slug)
                context={"products":product} 
                return render(request,"shop/search.html",context)
            
            else:
                messages.info(request,"No products found")
                #previous page
                return redirect(request.META.get("HTTP_REFERER"))

    #previous page
    return redirect(request.META.get("HTTP_REFERER"))    
      
