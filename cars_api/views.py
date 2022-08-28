from rest_framework import generics
from .serializer import CarSerializer
from .models import Car


class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
