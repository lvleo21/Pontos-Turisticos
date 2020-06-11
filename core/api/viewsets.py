from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    #Define como será a representação na API
    serializer_class = PontoTuristicoSerializer