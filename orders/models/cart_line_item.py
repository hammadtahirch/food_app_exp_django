from django.db import models

from orders.models.cart import Cart
from products.models.product import Product
from django.utils.translation import gettext_lazy as _


class CartLineItem(models.Model):
    class Meta:
        app_label = "orders"
        db_table = "cart_line_items"

    name = models.CharField(max_length=100, null=True, blank=True)
    unit_price = models.IntegerField(default=0)  # value will be save in cents
    quantity = models.IntegerField(default=0)  # value will be save in cents
    sub_total = models.IntegerField(default=0)  # value will be save in cents
    total = models.IntegerField(default=0)  # value will be save in cents
    cart = models.ForeignKey(Cart, verbose_name=_("cart_id"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("product_name"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
