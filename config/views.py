from django.db.models import Sum
from shipping.mock_data import MOCK_CARRIER_DATA
from purchases.models import Purchase, PurchasedItem
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response




class StatsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({
            'total_purchases': Purchase.objects.count(),
            'purchased_items': PurchasedItem.objects.aggregate(total=Sum('quantity'))['total'] or 0,
            'shipments': len(MOCK_CARRIER_DATA)
        })

