from rest_framework import serializers
from .models import Purchase, PurchasedItem



class PurchasedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedItem
        fields = '__all__'



class PurchaseSerializer(serializers.ModelSerializer):
    items = PurchasedItemSerializer(many=True, read_only=True)
    title = serializers.SerializerMethodField()
    country_name = serializers.CharField(source='country.name', read_only=True)
    continent = serializers.CharField(source='country.continent', read_only=True)

    class Meta:
        model = Purchase
        fields = '__all__'

    def get_title(self, obj):
        items = list(obj.items.all())
        if not items:
            return 'Empty purchase'
        if len(items) == 1:
            return items[0].product_name
        return f"{items[0].product_name} and {len(items) - 1} other book{'s' if len(items) > 2 else ''}"
