from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer
from rest_framework import status

class PontoTuristicoViewSet(ModelViewSet):
    
    #Define como será a representação na API
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("nome", "descricao")
    
    #define como serar a queryset do model
    def get_queryset(self):
        nome = self.request.query_params.get("nome", None)

        queryset = PontoTuristico.objects.all()

        if nome is not None:
            queryset = queryset.filter(nome = nome)


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

    # @action(methods=['get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     print(self.action_map)
    #     pass

    def list(self, request, *args, **kwargs):
        return  super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return  super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return  super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return  super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return  super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return  super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

