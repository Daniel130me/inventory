from django.contrib import admin
from .models import Product, Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'staff', 'quantity', 'date_odered']
    list_filter = ['product', 'staff', 'quantity', 'date_odered']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)