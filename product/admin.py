from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Products

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    ordering = ["id"]


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category", "price", "create", "available"]
    search_fields = ["name", "create"]
    ordering = ["id"]
