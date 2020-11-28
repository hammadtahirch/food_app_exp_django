from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from shops.models.shop import Shop
from system_settings.models.zone import Zone


class ShopSetting(models.Model):
    class Meta:
        app_label = "shops"
        db_table = "shop_settings"

    charge_to_shop = models.IntegerField(null=True)
    food_prep_time = models.IntegerField(null=True, blank=True)
    shop_rating = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=5, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE, primary_key=True)
    zone = models.ForeignKey(Zone, verbose_name=_("zone_id"), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.currency
