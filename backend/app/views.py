from django.shortcuts import render

# Import model
from .models import Service

# Import serializers
from .serializers import ServiceSerializer

# Import viewsets
from rest_framework import viewsets

# Create your views here.

class ServiceView(viewsets.ModelViewSet):
  # Get all services
  queryset = Service.objects.all()
  # Serializer class
  serializer_class = ServiceSerializer