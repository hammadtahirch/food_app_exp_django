from django.contrib import admin

# Register your models here.
from products.models import Product
from products.models.product_group import ProductGroup
from products.views.product_admin_view import ProductAdminView
from products.views.product_group_admin_view import ProductGroupAdminView

admin.site.register(Product, ProductAdminView)
admin.site.register(ProductGroup, ProductGroupAdminView)
