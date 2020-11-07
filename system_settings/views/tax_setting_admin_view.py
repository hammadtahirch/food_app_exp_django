from django.contrib import admin


class TaxSettingAdminView(admin.ModelAdmin):
    list_display = ("county_name", "province_name", "gst", "pst")
    list_filter = ("county_name", "province_name")
    search_fields = ("county_name", "province_name")