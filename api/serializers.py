from rest_framework import serializers
from vehicules.models import Vehicle, VehicleImage

class VehicleImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = VehicleImage
        fields = ['id', 'image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url) if obj.image else None


class VehicleSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    images = VehicleImageSerializer(many=True, read_only=True)  # images liées

    class Meta:
        model = Vehicle
        fields = ['id', 'nom', 'photo_url', 'marque', 'modele', 'carburant', 'kilometrage', 'annee', 'transmission', 'prix', 'photo', 'images']

        extra_kwargs = {
            'photo': {'write_only': True}
        }

    def get_photo_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.photo.url) if obj.photo else None
