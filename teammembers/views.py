from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeamMemberSerializer
from .models import TeamMember

# Create your views here.
class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
