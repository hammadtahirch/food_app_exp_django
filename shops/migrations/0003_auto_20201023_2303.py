# Generated by Django 3.0.5 on 2020-10-23 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_auto_20201023_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='province',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]