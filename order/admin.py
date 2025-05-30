from django.contrib import admin
from .models import OrderProduct, Order


# Register your models here.
class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0


# inlineAdmin funciona como un formulario dentro de otro
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInlineAdmin]
