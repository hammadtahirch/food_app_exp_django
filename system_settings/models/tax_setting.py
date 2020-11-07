from django.db import models


class TaxSetting(models.Model):
    class Meta:
        app_label = 'system_settings'
        db_table = 'tax_settings'

    county_name = models.CharField(max_length=25, null=True, blank=True)
    province_name = models.CharField(max_length=25, null=True, blank=True)
    gst = models.IntegerField(null=True, blank=True)
    pst = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.county_name + "," + self.province_name
