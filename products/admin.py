from django.contrib import admin

# Register your models here.
from products.models import Product, ProductVariance, ProductVarianceOption
from products.views.product_admin import ProductAdmin

admin.site.register(Product, ProductAdmin)
