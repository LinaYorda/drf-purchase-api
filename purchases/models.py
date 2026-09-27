from django.db import models

# Create your models here.

class Purchase(models.Model):
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey('countries.Country', on_delete=models.CASCADE)
    purchase_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        ordering = ['-purchase_date', 'id']


class PurchasedItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name = "items")
    product_name = models.CharField(max_length=255, blank=True, null=True)
    quantity= models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    