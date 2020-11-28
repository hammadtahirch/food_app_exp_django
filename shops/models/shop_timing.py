from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from shops.models.shop import Shop


class ShopTiming(models.Model):
    class Meta:
        app_label = "shops"
        db_table = "shop_timings"

    day = models.CharField(max_length=20)
    delivery_start_time = models.TimeField(null=True)
    delivery_end_time = models.TimeField(null=True)
    pick_up_start_time = models.TimeField(null=True)
    pick_up_end_time = models.TimeField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)
    shop = models.ForeignKey(Shop, verbose_name=_("shop_id"), on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['day', 'delivery_start_time', 'delivery_end_time', 'pick_up_start_time', 'pick_up_end_time',
                       'shop']

    def __str__(self):
        return self.day
