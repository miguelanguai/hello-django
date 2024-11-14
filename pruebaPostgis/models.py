from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.
class Sensor(models.Model):
    # Nombre del sensor
    nombre = models.CharField(max_length=100)
    
    # Temperatura del sensor
    temperatura = models.FloatField()
    
    # Humedad del sensor
    humedad = models.FloatField()
    
    # Ubicación geográfica del sensor
    ubicacion = geomodels.PointField()
    
    # Fecha de creación (opcional)
    fecha_creacion = models.DateTimeField(auto_now_add=True)