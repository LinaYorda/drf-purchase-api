from rest_framework import serializers
from .models import Purchase, PurchasedItem



class PurchasedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedItem
        fields = '__all__'
        extra_kwargs = {'purchase': {'read_only': True}}



class PurchaseSerializer(serializers.ModelSerializer):
    items = PurchasedItemSerializer(many=True, allow_empty=False)
    title = serializers.SerializerMethodField()
    country_name = serializers.CharField(source='country.name', read_only=True)
    continent = serializers.CharField(source='country.continent', read_only=True)

    class Meta:
        model = Purchase
        fields = '__all__'
        extra_kwargs = {'price': {'read_only': True}}

    def get_title(self, obj):
        items = list(obj.items.all())
        if not items:
            return 'Empty purchase'
        if len(items) == 1:
            return items[0].product_name
        return f"{items[0].product_name} and {len(items) - 1} other book{'s' if len(items) > 2 else ''}"

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        validated_data['price'] = sum(
            item['quantity'] * item['unit_price'] for item in items_data
        )
        purchase = Purchase.objects.create(**validated_data)
        PurchasedItem.objects.bulk_create([
            PurchasedItem(purchase=purchase, **item_data) for item_data in items_data
        ])
        return purchase
