from django.contrib import admin

# Register your models here.
from system_settings.models.email_template import EmailTemplate
from system_settings.models.tax_setting import TaxSetting
from system_settings.views.email_template_admin_view import EmailTemplateAdminView
from system_settings.views.tax_setting_admin_view import TaxSettingAdminView

admin.site.register(TaxSetting, TaxSettingAdminView)
admin.site.register(EmailTemplate, EmailTemplateAdminView)
