from rest_framework import serializers
from .models import Customer, Orders, Product
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields='__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields=['name','product']

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields='__all__'


class ProductSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False)
    orders = OrdersSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'






