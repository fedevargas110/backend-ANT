from django.urls import path
from LISTA.views import *

urlpatterns = [
  path('Guest/', GuestList.as_view(), name='guest'),
]