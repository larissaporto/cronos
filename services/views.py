from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ServiceSerializer
from .models import Service

# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('name')
    serializer_class = ServiceSerializer