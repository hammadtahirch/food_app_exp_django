from django.contrib import admin
import nested_admin
from products.views.product_variance_admin_view import ProductVarianceAdminView


class ProductAdminView(nested_admin.NestedModelAdmin):
    list_display = ("title", "description", "price", "is_published", "published_at", "is_active")
    list_filter = ("title", "description", "price", "is_published", "published_at", "is_active")
    search_fields = ("title__startswith", "price__startswith")
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None,
         {'fields':
              ("title", "description", "price", "is_published", "published_at", "is_active", "slug", "shop_id")}),
    )

    inlines = [
        ProductVarianceAdminView,
    ]
