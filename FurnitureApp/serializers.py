from rest_framework import serializers
from FurnitureApp.models import Product

class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
