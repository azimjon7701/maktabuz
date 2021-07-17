from django.shortcuts import render
from rest_framework import viewsets
from .models import Parent
from .serialisers import ParentSerializer
class ParentView(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer