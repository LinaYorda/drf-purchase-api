import random
import factory
from countries.models import Country
from purchases.models import Purchase, PurchasedItem
from django.core.management.base import BaseCommand
from seeding.book_data import random_book_title, realistic_price
from seeding.country_data import COUNTRIES


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = None
    country_code = None
    continent = None
    vat_rate = None


class PurchaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Purchase

    street_address = factory.Faker('street_address')
    city = factory.Faker('city')
    postal_code = factory.Faker('postcode')
    country = factory.SubFactory(CountryFactory)
    purchase_date = factory.Faker('date_this_decade')
    price = 0


class PurchasedItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PurchasedItem

    purchase = factory.SubFactory(PurchaseFactory)
    product_name = factory.LazyFunction(random_book_title)
    quantity = factory.Faker('random_int', min=1, max=10)
    unit_price = factory.LazyFunction(realistic_price)


def build_purchase_with_items(country):
    num_items = random.randint(1, 3)
    items_data = [
        (random_book_title(), random.randint(1, 5), realistic_price())
        for _ in range(num_items)
    ]
    total_price = round(sum(qty * price for _, qty, price in items_data), 2)

    purchase = PurchaseFactory(country=country, price=total_price)
    for product_name, quantity, unit_price in items_data:
        PurchasedItemFactory(purchase=purchase, product_name=product_name, quantity=quantity, unit_price=unit_price)
    return purchase


class Command(BaseCommand):
    help = "Seed the database with realistic countries, purchases and purchased items"

    def handle(self, *args, **options):
        PurchasedItem.objects.all().delete()
        Purchase.objects.all().delete()
        Country.objects.all().delete()

        countries = [
            CountryFactory(name=name, country_code=code, continent=continent, vat_rate=vat_rate)
            for name, code, continent, vat_rate in COUNTRIES
        ]
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(countries)} countries.'))

        purchases = [build_purchase_with_items(random.choice(countries)) for _ in range(1000)]
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(purchases)} purchases.'))

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {PurchasedItem.objects.count()} purchased items.'))
