from django.contrib import admin
from django import forms

from accounts.models.user import User
from shops.models import Shop


class ShopChangeFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user_ids = list(Shop.objects.values_list("user_id", flat=True).distinct())
        print(user_ids)
        self.fields['user_id'].queryset = User.objects.exclude(id__in=user_ids).filter(groups__name="shop_keeper")

    class Meta:
        model = Shop
        fields = (
            "name", "address", "city", "province", "country", "is_active", "slug", "user_id"
        )


class ShopAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "city", "province", "country", "is_active")
    list_filter = ("name", "address")
    search_fields = ("name__startswith", "address__startswith")

    form = ShopChangeFrom
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (None,
         {"fields": ("name", "address", "city", "province", "country", "is_active", "slug", "user_id")}
         ),
    )
