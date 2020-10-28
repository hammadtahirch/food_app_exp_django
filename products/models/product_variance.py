from django.db import models
from django.utils import timezone
from products.models import Product
from django.utils.translation import gettext_lazy as _


class ProductVariance(models.Model):
    class Meta:
        app_label = 'products'
        db_table = 'product_variances'

    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True, blank=True)
    max_permitted = models.SmallIntegerField(null=True, blank=True)
    min_permitted = models.SmallIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)
    product_id = models.ForeignKey(Product, verbose_name=_("product_id"), on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['title', 'product_id', 'description', 'max_permitted', 'min_permitted']

    def __str__(self):
        return self.title
