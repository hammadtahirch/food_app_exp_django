# Generated by Django 3.0.5 on 2020-11-11 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_auto_20201111_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='shop_name',
            new_name='name',
        ),
    ]
