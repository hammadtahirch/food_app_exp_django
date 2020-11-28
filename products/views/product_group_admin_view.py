from django.contrib import admin


class ProductGroupAdminView(admin.ModelAdmin):
    list_display = ("name", "description",)
    list_filter = ("name", "description",)
    search_fields = ("name__startswith",)
    fieldsets = (
        (None,
         {'fields':
             (
                 "name",
                 "description",
             )}),
    )
