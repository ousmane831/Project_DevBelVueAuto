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
    # Base URL dynamique selon l'environnement
    api_base_url = "https://project-devbelvueauto.onrender.com" if not request.get_host().startswith(('127.0.0.1', 'localhost')) else "http://127.0.0.1:8000"
    url = urljoin(api_base_url, f"/api/vehicules/{id}/")

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/json',
        }

        response = requests.get(
            url,
            headers=headers,
            cookies=request.COOKIES,
            timeout=10
        )

        if response.status_code != 200:
            raise Http404("Véhicule non trouvé")

        vehicle = response.json()

    except requests.RequestException as e:
        logger.error(f"Erreur lors de l'appel à l'API : {str(e)}")
        raise Http404("Service temporairement indisponible")

    # Récupération des images
    images = []
    if vehicle.get('photo_url'):
        images.append(vehicle['photo_url'])

    for img in vehicle.get('images', []):
        img_url = img.get('image_url') if isinstance(img, dict) else img
        if img_url and img_url not in images:
            images.append(img_url)

    return render(request, 'frontend/detail.html', {
        'vehicle': vehicle,
        'images': images
    })
