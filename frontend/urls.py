from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicules/', views.filter_view, name='filtrer_vehicules'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path("vehicle/<int:id>/", views.detail_vehicle, name="detail_vehicle")
]
