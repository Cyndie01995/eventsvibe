from django.shortcuts import render
from rest_framework import generics
from .models import Events, Registration
from rest_framework.permissions import IsAuthenticated
from .serializers import EventsSerializer, CustomUserSerializer

# Create your views here.
class EventsListView(generics.ListAPIView):
    serializer_class = EventsSerializer
    queryset = Events.objects.all() 


class EventsDetailView(generics.RetrieveAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class CustomUserCreateView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated)
          