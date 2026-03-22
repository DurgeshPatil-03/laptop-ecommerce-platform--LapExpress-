from django.contrib import admin
from .models import ProductModel

# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'processor', 'ram', 'rom', 'price']

admin.site.register(ProductModel, ProductModelAdmin)