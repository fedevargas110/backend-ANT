from rest_framework import serializers
from LISTA.models import People

class PeopleSerializer(serializers.ModelSerializer):
  class Meta:
    model = People
    fields = '__all__'