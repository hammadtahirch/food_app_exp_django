# Generated by Django 3.0.5 on 2020-11-20 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201120_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductGroup', verbose_name='product_group_id'),
        ),
    ]
