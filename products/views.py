from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.http.response import JsonResponse
from accounts .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def indexPage(request):
    return render (request, 'shop/index.html')



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
                    print('yes, it exists there!')
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
    else:
        pass 
    context={'cart':cart}
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