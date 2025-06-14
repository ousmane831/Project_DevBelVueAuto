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

def detail_vehicle(request, id):
    url = 'http://127.0.0.1:8000/api/filtrer/'
    response = requests.get(url)

    if response.status_code == 200:
        vehicules = response.json()
        vehicle = next((v for v in vehicules if v['id'] == id), None)

        if vehicle:
            images = []

            # Ajouter la photo principale s’il y en a une
            photo_url = vehicle.get('photo_url')
            if photo_url:
                images.append(photo_url)

            # Ajouter les images de la galerie
            for img in vehicle.get('images', []):
                image_url = img.get('image_url')
                if image_url and image_url != photo_url:  # éviter doublon
                    images.append(image_url)

            return render(request, 'frontend/detail.html', {
                'vehicle': vehicle,
                'images': images
            })

    return render(request, 'frontend/404.html', status=404)
