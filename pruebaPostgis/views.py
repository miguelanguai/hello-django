from rest_framework.decorators import api_view
from rest_framework.response import Response
from pruebaPostgis.models import Sensor
from .serializers import SensorSerializer

# Create your views here.

# GET de todos los sensores
@api_view(['GET'])
def getSensores(request):
    sensores = Sensor.objects.all()
    serializer = SensorSerializer(sensores, many=True)
    return Response(serializer.data)