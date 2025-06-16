from django.shortcuts import render



def home(request):
    return render(request, 'frontend/home.html')

def filter_view(request):
    return render(request, 'frontend/filter.html')

def services(request):
    return render(request, 'frontend/services.html')

def contact(request):
    return render(request, 'frontend/contact.html')


import requests
from django.shortcuts import render
from django.http import Http404
from urllib.parse import urljoin
import logging

logger = logging.getLogger(__name__)

def detail_vehicle(request, id):
    # Configuration unique pour tous les environnements
    api_base_url = "https://project-devbelvueauto.onrender.com" if not request.get_host().startswith(('127.0.0.1', 'localhost')) else "http://127.0.0.1:8000"
    
    # Essayer deux formats d'URL d'API possibles
    api_endpoints = [
        f"/api/vehicules/{id}/",  # Format préféré (nouveau)
        f"/api/filtrer/{id}/",     # Format alternatif
    ]
    
    vehicle = None
    last_exception = None
    
    for endpoint in api_endpoints:
        url = urljoin(api_base_url, endpoint)
        logger.debug(f"Essai avec l'URL: {url}")
        
        try:
            response = requests.get(url, timeout=10)
            logger.debug(f"Réponse: {response.status_code}")
            
            if response.status_code == 200:
                vehicle = response.json()
                if vehicle and 'id' in vehicle:
                    break  # Sortir de la boucle si véhicule trouvé
                    
        except requests.RequestException as e:
            last_exception = e
            continue  # Essayer le prochain endpoint
    
    # Si aucun endpoint n'a fonctionné
    if not vehicle:
        logger.error(f"Tous les endpoints API ont échoué. Dernière erreur: {str(last_exception)}")
        
        # Dernière tentative: récupérer tous les véhicules et filtrer localement
        try:
            fallback_url = urljoin(api_base_url, "/api/filtrer/")
            response = requests.get(fallback_url, timeout=10)
            all_vehicles = response.json()
            vehicle = next((v for v in all_vehicles if int(v.get('id')) == int(id)), None)
        except requests.RequestException as e:
            logger.error(f"Échec du fallback: {str(e)}")
            raise Http404("Service temporairement indisponible")
    
    if not vehicle:
        raise Http404("Ce véhicule n'existe pas")

    # Traitement des images
    images = []
    if vehicle.get('photo_url'):
        images.append(vehicle['photo_url'])
    
    for img in vehicle.get('images', []):
        if isinstance(img, dict) and img.get('image_url') and img['image_url'] not in images:
            images.append(img['image_url'])

    return render(request, 'frontend/detail.html', {
        'vehicle': vehicle,
        'images': images
    })