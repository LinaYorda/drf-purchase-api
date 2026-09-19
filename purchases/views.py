from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Purchase, PurchasedItem
from .serializers import PurchaseSerializer, PurchasedItemSerializer
from rest_framework.response import Response



# Create your views here.

class PurchasedItemDetailView(generics.RetrieveUpdateAPIView):
    queryset = PurchasedItem.objects.all()
    serializer_class = PurchasedItemSerializer



class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.prefetch_related('items')
    serializer_class = PurchaseSerializer

    @action(detail=True, methods=['post'])
    def refunds(self, request, pk=None):
        purchase = self.get_object()
        return Response({"status": "refunded", "purchase": purchase.id})
