from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  
  list_display = ('name', 'slug')
  prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'in_stock', 'created', 'updated')
  list_filter = ('in_stock', 'created', 'category')
  list_editable = ('price', 'in_stock')
  prepopulated_fields = {'slug': ('name',)}