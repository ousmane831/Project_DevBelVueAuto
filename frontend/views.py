from django.shortcuts import render



def home(request):
    return render(request, 'frontend/home.html')

def filter_view(request):
    return render(request, 'frontend/filter.html')

def services(request):
    return render(request, 'frontend/services.html')

def contact(request):
    return render(request, 'frontend/contact.html')


from django.shortcuts import render, get_object_or_404
from vehicules.models import Vehicle

def detail_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)

    images = []

    # ✅ Ajout de l’image principale
    if vehicle.photo:
        images.append(vehicle.photo.url)

    # ✅ Ajout des images liées via VehicleImage
    for img in vehicle.images.all():
        if img.image:
            images.append(img.image.url)

    return render(request, 'frontend/detail.html', {
        'vehicle': {
            'id': vehicle.id,
            'nom': vehicle.nom,
            'marque': vehicle.marque,
            'modele': vehicle.modele,
            'annee': vehicle.annee,
            'kilometrage': vehicle.kilometrage,
            'transmission': vehicle.transmission,
            'carburant': vehicle.carburant,
            'prix': vehicle.prix,
            'description': vehicle.description,
            'photo': vehicle.photo.url if vehicle.photo else None,
        },
        'images': images
    })
