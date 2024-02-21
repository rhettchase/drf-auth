from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Brew
from .permissions import IsOwnerOrReadOnly
from .serializers import BrewSerializer
from rest_framework.permissions import IsAuthenticated

class BrewList(ListCreateAPIView):
    # Anything that inherits from ListAPI View is going to need 2 brews.
    # What is the collection of brews, aka the queryset
    # associate collection of brews and the serial number
    queryset = Brew.objects.all()

    #serializing
    serializer_class = BrewSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly] # must be iterable

class BrewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Brew.objects.all()
    serializer_class = BrewSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly] # must be iterable


