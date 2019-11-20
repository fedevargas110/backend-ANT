from django.urls import path
from LISTA.views import *

urlpatterns = [
  path('People/', PeopleList.as_view(), name='people'),
]