# Generated by Django 3.0.5 on 2020-11-11 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_auto_20201111_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='user_id',
            new_name='user',
        ),
    ]
