from rest_framework import generics
from productos.serializers import ProductoSerializer
from productos.models import Producto

class ProductoListView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer



class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

