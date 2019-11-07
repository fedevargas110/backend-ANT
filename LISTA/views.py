from django.shortcuts import render, redirect
from LISTA.models import Guest
from LISTA.serializers import GuestSerializer
from rest_framework import viewsets, permissions, status
from rest_framework import filters

class GuestViewSet(viewsets.ModelViewSet):
  queryset = Guest.objects.all()
  serializer_class = GuestSerializer
  
  filter_backends = (filters.SearchFilter,)
  search_fields = ('name', 'dni', 'last_name')
