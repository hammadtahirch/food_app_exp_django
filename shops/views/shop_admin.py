from django.contrib import admin
from django import forms

from accounts.models.user import User
from shops.models import Shop
from shops.views.shop_timing_admin import ShopTimingAdmin


class ShopChangeFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_id'].queryset = User.objects.filter(groups__name="shop_keeper")

    class Meta:
        model = Shop
        fields = (
            "name", "slug", "address", "city", "province", "country", "is_active", "is_close", "user_id"
        )


class ShopAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "city", "province", "country", "is_active")
    list_filter = ("name", "address")
    search_fields = ("name__startswith", "address__startswith")

    form = ShopChangeFrom
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (None,
         {"fields": ("name", "slug", "address", "city", "province", "country", "is_active", "is_close", "user_id")}
         ),
    )
    inlines = [
        ShopTimingAdmin
    ]
