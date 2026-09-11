from rest_framework import serializers

# Serializer for shipping status data - sourced from an external API, no local model

class ShippingStatusSerializer(serializers.Serializer):
    tracking_number = serializers.CharField()                                                                                                                      
    carrier = serializers.CharField()                                                                                                                              
    status = serializers.CharField()                                                                                                                               
    estimated_delivery = serializers.DateField()       