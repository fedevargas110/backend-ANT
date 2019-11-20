from django.shortcuts import render, redirect
from LISTA.models import People
from LISTA.serializers import PeopleSerializer
from rest_framework import viewsets, permissions, status
from rest_framework import filters

class PeopleViewSet(viewsets.ModelViewSet):
  queryset = People.objects.all()
  serializer_class = PeopleSerializer
  
  filter_backends = (filters.SearchFilter,)
  search_fields = ('name', 'dni', 'last_name')
