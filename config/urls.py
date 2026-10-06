"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import auth_views
from .views import StatsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/csrf/', auth_views.csrf),
    path('api/login/', auth_views.login_view),
    path('api/logout/', auth_views.logout_view),
    path('api/me/', auth_views.me),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('purchases.urls')),
    path('api/', include('countries.urls')),
    path('api/', include('shipping.urls')),

    path('api/stats/',StatsView.as_view()),
]
