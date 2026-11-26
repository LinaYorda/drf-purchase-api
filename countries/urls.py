from django.urls import path
from .views import CountryListView, CountryAllListView

urlpatterns = [
    path('countries/', CountryListView.as_view(), name='country-list'),
    path('countries/all/', CountryAllListView.as_view(), name='country-all-list'),
]

