from django.db import models


class Zone(models.Model):
    class Meta:
        app_label = "system_settings"
        db_table = "zones"

    country_code = models.CharField(max_length=2, )
    zone_name = models.CharField(max_length=35, )

    def __str__(self):
        return self.zone_name
