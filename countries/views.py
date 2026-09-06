from django.shortcuts import render
from rest_framework import generics
from .models import Country
from .serializers import CountrySerializer

# Create your views here.

class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

