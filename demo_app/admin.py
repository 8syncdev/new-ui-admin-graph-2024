from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Product
# Register your models here.


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['name', 'price', 'created_at', 'updated_at']

    search_fields = ['name', 'price', 'description']
