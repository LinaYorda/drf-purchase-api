from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ShippingStatusSerializer
from .mock_data import MOCK_CARRIER_DATA

# Create your views here.

def fetch_shipping_status(tracking_number):

    """
    In a real app, this would call the carrier's API, e.g.:                                                                                                       
    response = requests.get(f"https://api.carrier.example/track/{tracking_number}")                                                                               
    return response.json()   
    """

    record = MOCK_CARRIER_DATA.get(tracking_number)
    if record is None:
        return None
    return {"tracking_number": tracking_number, **record}

class ShippingStatusView(APIView):
    def get(self, request, tracking_number):
        data = fetch_shipping_status(tracking_number)

        if data is None:
            return Response({"error": "Tracking number not found"}, status=404)
        serializer = ShippingStatusSerializer(data)
        return Response(serializer.data)

