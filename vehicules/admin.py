from django.contrib import admin
from .models import Vehicle
# Register your models here.

from django.contrib import admin
from .models import Vehicle, VehicleImage

class VehicleImageInline(admin.TabularInline):
    model = VehicleImage
    extra = 3  # Nombre d’images par défaut proposées dans l’admin

class VehicleAdmin(admin.ModelAdmin):
    inlines = [VehicleImageInline]

admin.site.register(Vehicle, VehicleAdmin)
