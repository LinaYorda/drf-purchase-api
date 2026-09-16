from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Purchase, PurchasedItem
from .serializers import PurchaseSerializer, PurchasedItemSerializer
from rest_framework.response import Response
from .permissions import IsManager
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class PurchasedItemDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PurchasedItem.objects.all()
    serializer_class = PurchasedItemSerializer



class PurchaseViewSet(viewsets.ModelViewSet):

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsManager()]

    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    @action(detail=True, methods=['post'])
    def refunds(self, request, pk=None):
        purchase = self.get_object()
        return Response({"status": "refunded", "purchase": purchase.id})
