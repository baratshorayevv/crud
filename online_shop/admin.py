from django.contrib import admin
from online_shop.models import Category
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'rating', 'discount', 'created_at', 'updated_at')
    list_filter = ('category', 'rating')
    search_fields = ('name', 'description')
