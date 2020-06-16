from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer
from rest_framework import status

class PontoTuristicoViewSet(ModelViewSet):
    
    #Define como será a representação na API
    serializer_class = PontoTuristicoSerializer
    
    #define como serar a queryset do model
    def get_queryset(self):
        queryset = PontoTuristico.objects.filter(aprovado = True)
        return queryset

    # retorna uma lista
    # def list(self,request, *args, **kwargs):
    #     pass

    # def create(self, request, *args, **kwargs):
    #     #para pegar um dado basta dar um request.data['nomeDoAtributo']
    #
    #     nome = request.data['nome']
    #     descricao = request.data['descricao']
    #
    #     aprovado = request.data.get("aprovado", default="false")
    #     aprovado = True if aprovado == "true" else False
    #
    #     try:
    #         ponto_turistico = PontoTuristico(nome=nome, descricao=descricao, aprovado=aprovado)
    #         ponto_turistico.save()
    #
    #         array = {
    #             "nome": nome,
    #             "descricao": descricao,
    #             "aprovado": aprovado,
    #         }
    #         return Response(array, status=status.HTTP_201_CREATED, )
    #     except:
    #         array = {
    #             "error": status.HTTP_400_BAD_REQUEST
    #         }
    #
    #         return Response(array, status=status.HTTP_400_BAD_REQUEST)


    # def destroy(self, request, *args, **kwargs):
    #     print(kwargs)
    #     PontoTuristico.objects.get(id = int(kwargs["pk"])).delete()
    #
    #     return Response(status= status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        print(self.action_map)
        pass
