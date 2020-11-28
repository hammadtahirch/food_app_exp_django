from django.db import models
from orders.models.cart_line_item import CartLineItem
from products.models.product_variance import ProductVariance
from django.utils.translation import gettext_lazy as _


class CartLineItemOption(models.Model):
    class Meta:
        app_label = "orders"
        db_table = "cart_line_item_options"

    name = models.CharField(max_length=100, null=True, blank=True)
    unit_price = models.IntegerField(default=0, blank=True)  # value will be save in cents
    quantity = models.IntegerField(default=0, blank=True)  # value will be save in cents
    productVariance = models.ForeignKey(ProductVariance, verbose_name=_("product_variance_id"),
                                        on_delete=models.CASCADE)
    CartLineItem = models.ForeignKey(CartLineItem, verbose_name=_("cart_line_item_id"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
