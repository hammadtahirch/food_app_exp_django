# Generated by Django 3.0.5 on 2020-10-31 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0007_auto_20201031_0303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoptiming',
            old_name='user_id',
            new_name='shop_id',
        ),
    ]
