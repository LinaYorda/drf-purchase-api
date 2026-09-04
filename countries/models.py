from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.TextField(blank=True, null=True)
    local_address = models.CharField(max_length=255, blank=True, null=True)
    local_code= models.CharField(max_length=100, blank=True, null=True)
    country_code = models.CharField(max_length=100, blank=True, null=True)
    local_vat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)




