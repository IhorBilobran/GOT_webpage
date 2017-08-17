from rest_framework import serializers

from shop.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'img')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
                'id', 'name', 'description', 'img',
                'available', 'price', 'created', 'updated',
                'reference', 'category'
            )
