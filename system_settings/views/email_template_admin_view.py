from django.contrib import admin


class EmailTemplateAdminView(admin.ModelAdmin):
    list_display = ("subject", "template_key",)
    list_filter = ("subject", "template_key",)
    search_fields = ("subject", "template_key",)
