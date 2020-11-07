from django.db import models
from djrichtextfield.models import RichTextField


class EmailTemplate(models.Model):
    class Meta:
        app_label = "system_settings"
        db_table = "email_templates"

    subject = models.CharField(max_length=255, null=True, blank=True)
    template_body = RichTextField(null=True, blank=True)
    template_key = models.CharField(max_length=255, null=True, blank=True)
    tokens = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.subject
