''' Documenting imports at the beginning of file '''
import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from products.models import Product
from profiles.models import UserProfile

# Storing Models for secure checkout of shopping Cart.


class Order(models.Model):
    '''Model for entering delivery details'''
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    mobile = models.CharField(max_length=20, null=False, blank=False)
    address_line1 = models.CharField(max_length=80, null=False, blank=False)
    address_line2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=16, null=True, blank=True)
    eircode = models.CharField(max_length=8, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )
    delivery_cost = 7
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254,
                                  null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        """
        Unique order number genrated using UUID, only used in this class.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Aggregate function used to update grand total each time a
        product is added to shopping cart, including adding the delivery costs.
        """
        self.total = self.cartitems.aggregate(
            Sum('cart_total'))['cart_total__sum'] or 0
        self.grand_total = self.total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Generates order number if the field is blank.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class CartItem(models.Model):
    '''
        Model for individual shopping cart items
        in each order
    '''
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='cartitems'
        )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
        )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    cart_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
        )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the cartitem total
        and update the order total.
        """
        self.cart_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
