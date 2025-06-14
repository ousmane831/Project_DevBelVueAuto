from rest_framework import viewsets
from vehicules.models import Vehicle
from .serializers import VehicleSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all().order_by('-id')
    serializer_class = VehicleSerializer
    parser_classes = [MultiPartParser, FormParser]

   # views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def filtrer_vehicules(request):
    vehicules = Vehicle.objects.all()

    marque = request.GET.get('marque')
    modele = request.GET.get('modele')
    carburant = request.GET.get('carburant')
    transmission = request.GET.get('transmission')
    annee = request.GET.get('annee')
    kilometrage = request.GET.get('kilometrage')
    prix_max = request.GET.get('prix_max')

    if marque:
        vehicules = vehicules.filter(marque__iexact=marque)
    if modele:
        vehicules = vehicules.filter(modele__iexact=modele)
    if carburant:
        vehicules = vehicules.filter(carburant__iexact=carburant)
    if transmission:
        vehicules = vehicules.filter(transmission__iexact=transmission)
    if annee:
        vehicules = vehicules.filter(annee__lte=annee)
    if kilometrage:
        vehicules = vehicules.filter(kilometrage__lte=kilometrage)
    if prix_max:
        vehicules = vehicules.filter(prix__lte=prix_max)

    serializer = VehicleSerializer(vehicules, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def get_modeles_par_marque(request):
    marque = request.GET.get('marque')
    if not marque:
        return Response([])

    modeles = Vehicle.objects.filter(marque__iexact=marque).values_list('modele', flat=True).distinct()
    return Response(modeles)
