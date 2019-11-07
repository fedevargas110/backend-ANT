from django.shortcuts import render, redirect
from LISTA.models import Guest
from LISTA.serializers import GuestSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import filters
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.authentication import TokenAuthentication, SessionAuthentication

class GuestViewSet(viewsets.ModelViewSet):
#  permission_classes = (IsAuthenticated,)
#  authentication_classes = (TokenAuthentication, SessionAuthentication)
  queryset = Guest.objects.all()
  serializer_class = GuestSerializer
  
  filter_backends = (filters.SearchFilter,)
  search_fields = ('name', 'dni', 'last_name')
