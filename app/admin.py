from django.contrib import admin
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced
)
# Register your models here.


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_dispaly = ['id', 'user', 'name',
                    'locality', 'city', 'zipcode', 'state']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_dispaly = ['id', 'title', 'selling_price', 'discounted_prices',
                    'description', 'brand', 'category', 'product_image']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_dispaly = ['id', 'user', 'product',
                    'quantity']


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_dispaly = ['id', 'user', 'customer', 'product',
                    'quantity', 'ordered_date', 'status']
