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
    # Configuration des URLs API
    host = request.get_host().split(':')[0]
    if host in ("127.0.0.1", "localhost"):
        api_base_url = "http://127.0.0.1:8000"
        api_endpoint = "/api/filtrer/"  # Endpoint local qui retourne tous les véhicules
    else:
        api_base_url = "https://project-devbelvueauto.onrender.com"
        api_endpoint = f"/api/filtrer/{id}/"  # Endpoint production avec ID

    url = urljoin(api_base_url, api_endpoint)
    
    logger.debug(f"Tentative de récupération du véhicule via URL: {url}")

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Gestion des deux formats de réponse (liste ou objet unique)
        if host in ("127.0.0.1", "localhost"):
            # Mode local - on reçoit une liste de véhicules
            vehicle = next((v for v in data if int(v.get('id')) == int(id)), None)
        else:
            # Mode production - on reçoit directement le véhicule
            vehicle = data if data and 'id' in data else None

        if not vehicle:
            logger.warning(f"Véhicule {id} non trouvé dans la réponse API")
            raise Http404("Ce véhicule n'existe pas")

    except requests.exceptions.HTTPError as e:
        logger.error(f"Erreur HTTP de l'API: {str(e)}")
        if e.response.status_code == 404:
            raise Http404("Ce véhicule n'existe pas")
        raise Http404("Erreur temporaire du serveur, veuillez réessayer plus tard")
    except requests.RequestException as e:
        logger.error(f"Erreur de connexion à l'API: {str(e)}")
        raise Http404("Service temporairement indisponible")

    # Traitement des images (inchangé)
    images = []
    photo_url = vehicle.get('photo_url')
    if photo_url:
        images.append(photo_url)

    for img in vehicle.get('images', []):
        image_url = img.get('image_url')
        if image_url and image_url != photo_url:
            images.append(image_url)

    return render(request, 'frontend/detail.html', {
        'vehicle': vehicle,
        'images': images
    })