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

def detail_vehicle(request, id):
    # Détection base URL API
    host = request.get_host()
    if host.startswith("127.0.0.1") or host.startswith("localhost"):
        api_base_url = "http://127.0.0.1:8000"
    else:
        api_base_url = "https://project-devbelvueauto.onrender.com"

    url = f"{api_base_url}/api/filtrer/"
    
    try:
        response = requests.get(url, timeout=5)  # Timeout pour éviter blocage
        response.raise_for_status()  # Lève une exception en cas d'erreur HTTP
    except requests.RequestException:
        raise Http404("Erreur lors de la récupération des données du véhicule")

    vehicules = response.json()
    vehicle = next((v for v in vehicules if v['id'] == id), None)

    if not vehicle:
        raise Http404("Véhicule non trouvé")

    images = []
    photo_url = vehicle.get('photo_url')
    if photo_url:
        images.append(photo_url)

    # Ajouter images supplémentaires sans doublon
    for img in vehicle.get('images', []):
        image_url = img.get('image_url')
        if image_url and image_url != photo_url:
            images.append(image_url)

    return render(request, 'frontend/detail.html', {
        'vehicle': vehicle,
        'images': images
    })
