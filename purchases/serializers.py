from rest_framework import serializers
from .models import Purchase, PurchasedItem



class PurchasedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedItem
        fields = '__all__'



class PurchaseSerializer(serializers.ModelSerializer):
    items = PurchasedItemSerializer(many=True, read_only=True)
    class Meta:
        model = Purchase
        fields = '__all__'


