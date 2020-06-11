from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)