from django.db import models
from django.utils import timezone


class ProductGroup(models.Model):
    class Meta:
        app_label = 'products'
        db_table = 'product_groups'

    name = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
