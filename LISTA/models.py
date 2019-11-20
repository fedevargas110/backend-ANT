from django.db import models

# Create your models here.

class People(models.Model):
  id_people = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20, null=False)
  last_name = models.CharField(max_length=20, null=False)
  dni = models.CharField(max_length=8, null=False)
  attended = models.BooleanField(default=False)
  def __str__(self):
    return '{}, {}, {}'.format(self.name, self.last_name, self.dni)