from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
  list_display = ('name','last_name','dni')
  list_filter = ('name','last_name')