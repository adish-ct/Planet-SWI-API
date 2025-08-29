from rest_framework.viewsets import ModelViewSet
from .serializers import PlanetSerializer
from .models import Planet

# Create your views here.

class PlanetViewSet(ModelViewSet):
    """
    This performs POST, GET, PUT/PATCH, DELETE Restful endpoints
    """
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

