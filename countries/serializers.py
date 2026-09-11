from rest_framework import serializers
from .models import Country


# Serializer for the Country model

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


