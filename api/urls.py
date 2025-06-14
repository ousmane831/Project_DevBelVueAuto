from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import VehicleViewSet, filtrer_vehicules, get_modeles_par_marque

router = DefaultRouter()
router.register(r"vehicules", VehicleViewSet)

urlpatterns = [
    path("filtrer/", filtrer_vehicules, name="filtrer_vehicules"),
    path('api/modeles/', get_modeles_par_marque, name='get_modeles_par_marque'),
    path("", include(router.urls)),
]
