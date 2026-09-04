import random
import factory
from countries.models import Country
from purchases.models import Purchase, PurchasedItem
from django.core.management.base import BaseCommand









class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = factory.Faker('country')
    local_address = factory.Faker('address')
    local_code = factory.Faker('postcode')
    country_code = factory.Faker('country_code')
    local_vat = factory.Faker('pydecimal', left_digits=2, right_digits=2, positive=True)

class PurchaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Purchase

    title = factory.Faker('sentence', nb_words=3)                                                                                                                  
    city = factory.Faker('city')                                                                                                                                   
    country = factory.SubFactory(CountryFactory)
    continent = factory.Faker('random_element', elements=['Europe', 'Asia', 'Africa', 'North America', 'South America', 'Oceania'])                                
    purchase_date = factory.Faker('date_this_decade')                                                                                                              
    price = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True) 


class PurchasedItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PurchasedItem

    purchase = factory.SubFactory(PurchaseFactory)
    product_name = factory.Faker('sentence', nb_words=4)
    quantity = factory.Faker('random_int', min=1, max=10)
    unit_price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)


class Command(BaseCommand):
    help = "Seed the database with 100 realistic rows per table using factory_boy and Faker"


    def handle(self, *args, **options):
        PurchasedItem.objects.all().delete()
        Purchase.objects.all().delete()
        Country.objects.all().delete()

        countries = CountryFactory.create_batch(1000)
        self.stdout.write(self.style.SUCCESS('Successfully seeded 1000 countries.'))

        purchases = PurchaseFactory.create_batch(1000)
        self.stdout.write(self.style.SUCCESS('Successfully seeded 1000 purchases.'))

        items = PurchasedItemFactory.create_batch(1000)
        self.stdout.write(self.style.SUCCESS('Successfully seeded 1000 purchased items.'))
