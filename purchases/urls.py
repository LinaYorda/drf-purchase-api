from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PurchasedItemDetailView, PurchaseViewSet

router = DefaultRouter()
router.register(r'purchases', PurchaseViewSet, basename='purchase')

urlpatterns = [
    path('', include(router.urls)),
    path('purchased-items/<int:pk>/', PurchasedItemDetailView.as_view(), name='purchased-item-detail'),
]
