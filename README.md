# Django REST API Purchase Management System

A full-stack purchase management system for a small book shop, with a Django REST Framework backend and a Vue.js frontend that consumes the API.


<table>
  <tr>
    <td><img src="docs/screenshots/drf-purchase-api-login.png" width="400" alt="Login page"></td>
    <td><img src="docs/screenshots/drf-purchase-api-countries-table.png" width="400" alt="Countries table"></td>
  </tr>
  <tr>
    <td><img src="docs/screenshots/drf-purchase-api-purchases-table.png" width="400" alt="Purchases table"></td>
    <td><img src="docs/screenshots/drf-purchase-api-shipping-status-table.png" width="400" alt="Shipping status lookup"></td>
  </tr>
</table>



## Used Stack

- Django and Django REST Framework (REST API)
- SQLite
- Vue.js 3 (Vite), Vue Router, TanStack Table
- Tailwind CSS and daisyUI
- uv package manager (Python), npm (frontend)

## Setup

**Prerequisites:** Python 3.13, [uv](https://docs.astral.sh/uv/), Node.js

### Backend

```bash
git clone https://github.com/LinaYorda/drf-purchase-api.git
cd drf-purchase-api
uv sync
cp .env.example .env    # fill in your own SECRET_KEY
python manage.py migrate
python manage.py mock_data_simulator      # optional: seeds countries/purchases/purchased items
python manage.py seed_shipping_mock_data  # optional: generates fake shipping tracking data
python manage.py runserver                # http://localhost:8000
```

### Frontend

In a second terminal, with the backend running:

```bash
cd frontend
npm install
npm run dev      # http://localhost:5173
```

The frontend calls the API at `http://localhost:8000`, so the backend must be running for the tables to load.

### Environment variables

Set these in `.env` (see `.env.example`):

| Variable | Description |
|---|---|
| `SECRET_KEY` | Required. Django will not start without it. |
| `DEBUG` | `True` for local development. Defaults to `False`. |
| `ALLOWED_HOSTS` | Comma-separated list, e.g. `localhost,127.0.0.1`. |

### CORS

The browser only lets the frontend call the API because `http://localhost:5173` is listed in `CORS_ALLOWED_ORIGINS` in `config/settings.py`. If you run the frontend on a different port, add that origin there, or requests will fail with a CORS error.

## API Endpoints

All endpoints are under `/api/`. List endpoints are paginated (100 per page, use `?page=2`).

| Endpoint | Description |
|---|---|
| `/api/countries/` | List of countries |
| `/api/purchases/` | List and create purchases (router-based viewset) |
| `/api/purchased-items/<id>/` | Purchased item detail |
| `/api/shipping-status/<tracking_number>/` | Shipping status by tracking number |

## Project Structure

**Backend**

- purchases/ — core purchase/order logic; mock data generated with Faker.
- countries/ — country reference data; mock data generated with Faker.
- shipping/ — shipping-related models and logic; mock data generated with Faker.
- seeding/ — management commands for populating demo/test data.
- config/ — Django project settings, URLs, WSGI/ASGI entry points.

**Frontend** (`frontend/src/`)

- views/ — pages (Home, Countries, Purchases, Login).
- components/ — shared layout pieces (Header, Sidebar, Footer).
- router/ — route definitions.
- App.vue — page shell: header, collapsible sidebar (daisyUI drawer), content area, footer.

## Status

🚧 Work in progress.

Done:

- Django + DRF project scaffolding
- Base apps: purchases, countries, shipping
- Data seeding setup
- API endpoints for countries and purchases, with pagination
- Vue frontend with routing, a collapsible sidebar, and paginated Countries and Purchases tables
- CORS configuration for the local frontend

Planned:

- Search on the tables (the search box is in the UI, backend filtering is not implemented yet)
- Login and authentication, with the dashboard visible only to logged-in users
- Show country names instead of IDs in the Purchases table
- Frontend pages for purchased items and shipping

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
