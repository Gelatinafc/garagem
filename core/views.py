from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Marca, Carro
from core.serializers import CategoriaSerializer, MarcaSerializer, CarroSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CarroViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
