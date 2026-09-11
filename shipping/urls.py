from django.urls import path
from .views import ShippingStatusView


urlpatterns = [
    path('shipping-status/<str:tracking_number>/', ShippingStatusView.as_view(), name='shipping-status'),
]