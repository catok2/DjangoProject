from django.shortcuts import render
from rest_framework import viewsets
from .models import Products
from .serializers import Productserializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = Productserializer
