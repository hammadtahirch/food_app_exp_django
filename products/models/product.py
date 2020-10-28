from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from shops.models.shop import Shop


class Product(models.Model):
    class Meta:
        app_label = 'products'
        db_table = 'products'

    title = models.CharField(max_length=255, null=True)
    slug = models.CharField(max_length=255, null=True, unique=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    is_published = models.BooleanField(default=0)
    published_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=0, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)
    shop_id = models.ForeignKey(Shop, verbose_name=_("shop_id"), on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['title', 'description', 'price']

    def __str__(self):
        return self.title
