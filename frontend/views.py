from django.shortcuts import render



def home(request):
    return render(request, 'frontend/home.html')

def filter_view(request):
    return render(request, 'frontend/filter.html')

def services(request):
    return render(request, 'frontend/services.html')

def contact(request):
    return render(request, 'frontend/contact.html')



import os
import requests
from django.shortcuts import render

def detail_vehicle(request, id):
    # Choix de l'URL de l'API selon l'environnement (local ou production)
    if request.get_host().startswith("127.0.0.1") or request.get_host().startswith("localhost"):
        api_base_url = "http://127.0.0.1:8000"
    else:
        api_base_url = "https://project-devbelvueauto.onrender.com"

    url = f"{api_base_url}/api/filtrer/"
    response = requests.get(url)

    if response.status_code == 200:
        vehicules = response.json()
        vehicle = next((v for v in vehicules if v['id'] == id), None)

        if vehicle:
            images = []

            # Ajouter la photo principale si elle existe
            photo_url = vehicle.get('photo_url')
            if photo_url:
                images.append(photo_url)

            # Ajouter les images supplémentaires sans doublon
            for img in vehicle.get('images', []):
                image_url = img.get('image_url')
                if image_url and image_url != photo_url:
                    images.append(image_url)

            return render(request, 'frontend/detail.html', {
                'vehicle': vehicle,
                'images': images
            })

    # Si le véhicule n'existe pas ou erreur API, afficher la page 404
    return render(request, 'frontend/404.html', status=404)
