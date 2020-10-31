from django.contrib import admin
import nested_admin
from products.models import ProductVariance
from products.views.product_variance_option_admin import ProductVarianceOptionAdmin


class ProductVarianceAdmin(nested_admin.NestedTabularInline):
    model = ProductVariance
    extra = 1
    list_display = ("title", "description", "max_permitted", "min_permitted", "product_id")
    list_filter = ("title", "description", "max_permitted", "min_permitted", "product_id")
    fieldsets = (
        (None,
         {'fields':
             (
                 "title",
                 "description",
                 "max_permitted",
                 "min_permitted",
                 "product_id"
             )}),
    )

    inlines = [
        ProductVarianceOptionAdmin
    ]
