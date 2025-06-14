from django.db import models

class Vehicle(models.Model):
    TRANSMISSIONS = [
        ('Manuelle', 'Manuelle'),
        ('Automatique', 'Automatique'),
    ]
    
    CARBURANTS = [
        ('Essence', 'Essence'),
        ('Hybride', 'Hybride'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Gasoil', 'Gasoil'),
    ]

    MARQUES = [
        ('DS Automobiles', 'DS Automobiles'),
        ('BMW', 'BMW'),
        ('Mercedes Benz', 'Mercedes Benz'),
        ('Land Rover', 'Land Rover'),
        ('Opel', 'Opel'),
        ('Citroën', 'Citroën'),
        ('Lamborghini', 'Lamborghini'),
    ]

    MODELES = [
        ('DS 7 Crossback E-Tense', 'DS 7 Crossback E-Tense'),
        ('DS 3', 'DS 3'),
        ('Grand lander', ' Grand lander'),
        ('Crossland', 'Crossland'),
        ('XM', 'XM'),
        ('Range Rover Sport', 'Range Rover Sport'),
        ('Range Rover Velar', 'Range Rover Velar'),
        ('Classe GT', 'Classe GT'),
        ('Classe GLE 53', 'Classe GLE 53'),
        ('Classe S63', 'Classe S63'),
        ('URUS', 'URUS'),
        ('C4X Ë série', 'C4X Ë série'),
        ('Aventador SV Roadster', 'Aventador SV Roadster'),
    ]

    nom = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='vehicules/')
    marque = models.CharField(max_length=50, choices=MARQUES)
    modele = models.CharField(max_length=50, choices=MODELES)
    carburant = models.CharField(max_length=50, choices=CARBURANTS, default='Essence')
    kilometrage = models.PositiveIntegerField()
    annee = models.PositiveIntegerField()
    transmission = models.CharField(max_length=50, choices=TRANSMISSIONS)
    prix = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, blank=True)


    def __str__(self):
        return f"{self.nom} - {self.marque} {self.modele}"
    
class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='vehicules/gallery/')
    
    def __str__(self):
        return f"Image de {self.vehicle.nom}"

