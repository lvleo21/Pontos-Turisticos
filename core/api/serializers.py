from rest_framework.serializers import ModelSerializer #1
from core.models import PontoTuristico #2

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ["id", "nome", "descricao"]