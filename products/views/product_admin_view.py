from django.contrib import admin
import nested_admin
from products.views.product_variance_admin_view import ProductVarianceAdminView


class ProductAdminView(nested_admin.NestedModelAdmin):
    list_display = ("title", "price", "is_published", "published_at", "is_active")
    list_filter = ("title", "price", "is_published", "published_at", "is_active")
    search_fields = ("title__startswith", "price__startswith")
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None,
         {'fields':
             (
                 "title",
                 "description",
                 "price",
                 "image_url",
                 "is_published",
                 "published_at",
                 "is_active",
                 "slug",
                 "shop",
                 "product_group",
             )}),
    )

    inlines = [
        ProductVarianceAdminView,
    ]
