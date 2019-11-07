from django.db import models

# Create your models here.

class Guest(models.Model):
  id_guest = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20, null=False)
  last_name = models.CharField(max_length=20, null=False)
  dni = models.CharField(max_length=8, null=False)
  def __str__(self):
    return '{}, {}, {}'.format(self.name, self.last_name, self.dni)