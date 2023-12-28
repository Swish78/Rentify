# core/views.py

from django.shortcuts import render
from rest_framework import generics
from .models import ToolItem
from .serializers import ItemSerializer


# Create your views here.


class ItemListCreateView(generics.ListCreateAPIView):
    queryset = ToolItem.objects.all()
    serializer_class = ItemSerializer


class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToolItem.objects.all()
    serializer_class = ItemSerializer
