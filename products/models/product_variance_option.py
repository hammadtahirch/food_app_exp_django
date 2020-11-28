from django.db import models
from django.utils import timezone

from products.models import ProductVariance
from django.utils.translation import gettext_lazy as _


class ProductVarianceOption(models.Model):
    class Meta:
        app_label = 'products'
        db_table = 'product_variance_options'

    title = models.CharField(max_length=255, null=True)
    component_price = models.DecimalField(max_digits=65, default=0, decimal_places=2)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)
    variance = models.ForeignKey(ProductVariance, verbose_name=_("variance_id"), on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['title', 'component_price', 'variance_id']

    def __str__(self):
        return self.title
