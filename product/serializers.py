from rest_framework import serializers

from .models import  *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):

    """Serializer for the Cart model."""

    # customer = UserSerializer(read_only=True)
    # used to represent the target of the relationship using its __unicode__ method
    # items = serializers.StringRelatedField(many=True)
    # product = ProductSerializer(read_only=True)
    

    class Meta:
        model = Cart
        fields = ('id', 'customer', 'created_at', 'product')

class OrderSerializer(serializers.ModelSerializer):

    """Serializer for the Order model."""

    # customer = UserSerializer(read_only=True)
    # used to represent the target of the relationship using its __unicode__ method
    # order_items = serializers.StringRelatedField(many=True, required=False)
    # cart = CartSerializer(read_only=True)

    class Meta:
        model = Order
        fields = (
            'id', 'customer', 'created_at', 'cart'
        )

