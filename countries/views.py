from django.shortcuts import render
from rest_framework import generics
from .models import Country
from .serializers import CountrySerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CountryListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

