from django.shortcuts import render,redirect
from products.models import Product
from .models import CartItem
from user.models import User


# Create your views here.
def add_to_cart(request,product_id):
    product = Product.objects.get(pk=product_id)
    user=request.user
    # username=User.objects.get(username=user)
    cart_item,create=CartItem.objects.get_or_create(product=product,user=user)
    if not create:
        cart_item.quantity += 1
        cart_item.save()
    return render(request,'cart/cart.html',{'product_id':product_id})


def cart_view(request,username):
    username=User.objects.get(username=username)
    cart_item=CartItem.objects.filter(user=username)
    return render(request,'cart/cart.html',{'cart_item':cart_item,'user':username})