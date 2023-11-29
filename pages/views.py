from django.shortcuts import render
from products.models import Product

# Create your views here.
def homeView(request):
    products = Product.objects.all()
    return render(request, 'pages/home.html', {'products': products})


def landingView(request):
    return render(request, 'pages/landing-page.html',{})

def aboutUsView(request):
    return render(request, 'pages/about-us.html',{})
def contactUsView(request):
    return render(request, 'pages/contact-us.html',{})