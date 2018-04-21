from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    # class Meta:
    #     model = Product
    #     fields = ('name')
    #     #fields = '__all__'

