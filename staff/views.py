from django.shortcuts import render
from rest_framework import viewsets
from .models import Staff
from .serializers import StaffSerializer
class StaffView(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer