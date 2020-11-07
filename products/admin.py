from django.contrib import admin

# Register your models here.
from products.models import Product
from products.views.product_admin_view import ProductAdminView

admin.site.register(Product, ProductAdminView)
