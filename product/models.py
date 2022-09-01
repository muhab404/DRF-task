from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('price',)
    
    def __str__(self):
        return self.name


class Cart(models.Model):
    """A model that contains data for a shopping cart."""
    customer = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField(
        Product,
        related_name='items',
    )
    def __str__(self):
        return f'{self.customer} cart'


class Order(models.Model):
    """
    An Order is the more permanent counterpart of the shopping cart. It represents
    the frozen the state of the cart on the moment of a purchase. In other words,
    an order is a customer purchase.
    """
    customer = models.ForeignKey(
        User,
        related_name='orders',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(
        Cart,
        related_name='order_items',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f'{self.customer} order'