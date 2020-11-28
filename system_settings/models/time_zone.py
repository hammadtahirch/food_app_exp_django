from django.db import models

from system_settings.models.zone import Zone
from django.utils.translation import gettext_lazy as _


class TimeZone(models.Model):
    class Meta:
        app_label = "system_settings"
        db_table = "time_zones"

    zone = models.ForeignKey(Zone, verbose_name=_("zone_id"), on_delete=models.CASCADE)
    abbreviation = models.CharField(max_length=6)
    time_start = models.FloatField(max_length=11)
    gmt_offset = models.IntegerField()
    dst = models.CharField(max_length=1)

    def __str__(self):
        return self.abbreviation
