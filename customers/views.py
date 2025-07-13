from django.shortcuts import render
from .models import*
from .serializers import*
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.

# views using modelviewset

class customerviews(viewsets.ModelViewSet):
    queryset = customers.objects.all()
    serializer_class = CustomerSerializer
    