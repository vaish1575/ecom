from django.urls import path
from .views import homeView,landingView,aboutUsView,contactUsView

urlpatterns = [
    path('',landingView ,name='landing'),
    path('home/',homeView,name='home'),
    path('contactus/',contactUsView,name='contact-us'),
    path('aboutus/',aboutUsView,name='about-us'),
]