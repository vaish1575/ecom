from django.urls import path
from .views import add_to_cart,cart_view
urlpatterns=[
    path('add_to_cart/<int:product_id>/',add_to_cart,name='addToCart'),
    path('cart/<str:username>/', cart_view, name='cart'),
]
