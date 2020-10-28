from django.contrib import admin
import nested_admin
from products.models import ProductVarianceOption


class ProductVarianceOptionAdmin(nested_admin.NestedTabularInline):
    model = ProductVarianceOption
    extra = 1
    list_display = ("title", "component_price", "variance_id")
    list_filter = ("title", "component_price", "variance_id")
    fieldsets = (
        (None,
         {'fields':("title", "component_price", "variance_id")}),)
