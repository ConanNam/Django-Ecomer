from django.contrib import admin
from .models import *


admin.site.register(
    [Admin, Customer, Category, Product, Publisher ,Producer, Type, Book, MobilePhone, Clothe, Laptop, Shoe, Electronic, Cart, CartProduct, Order, ProductImage])
    # , Publisher ,Producer , Type
