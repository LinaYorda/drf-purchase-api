# Django REST API Purchase Managment System


A full-stack purchase management system for a small book shop, with a Django REST Framework backend and a frontend planned to consume the API.

## Used Stack 
- REST API
- SQLite
- Frontend(still in discussion)
- uv package manager

## Setup 

**Prerequisites:** Python 3.13, [uv](https://docs.astral.sh/uv/)

```bash
git clone https://github.com/LinaYorda/drf-purchase-api.git
cd drf-purchase-api
uv sync
cp .env.example .env    # fill in your own SECRET_KEY
python manage.py migrate
python manage.py mock_data_simulator      # optional: seeds countries/purchases/purchased items 
python manage.py seed_shipping_mock_data  # optional: generates fake shipping tracking data
python manage.py runserver
```

## Project Structure

- purchases/ — core purchase/order logic; mock data generated with Faker.
- countries/ — country reference data; mock data generated with Faker.
- shipping/ — shipping-related models and logic; mock data generated with Faker.
- seeding/ — management commands for populating demo/test data.
- config/ — Django project settings, URLs, WSGI/ASGI entry points.

## Status 

🚧 Work in progress — API endpoints and frontend not yet finalized.

Done:

- Django + DRF project scaffolding
- Base apps: purchases, countries, shipping
Data seeding setup

Planned:

- API endpoints for purchases
Frontend (TBD)


## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.



