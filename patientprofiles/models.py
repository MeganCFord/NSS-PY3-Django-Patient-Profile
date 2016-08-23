from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# Medication
class Medication(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=2000)
  def __str__(self):
    return (self.name)

# Ailment
class Ailment(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=2000)
  medication = models.ManyToManyField(Medication, blank=True)
  def __str__(self):
    return self.name

# Patient
class Patient(models.Model):
  name = models.CharField(max_length=200)
  birthday = models.DateField("birthday")
  last_seen = models.DateTimeField("last appointment") 
  ailments = models.ManyToManyField(Ailment, blank=True)
  def __str__(self):
    return self.name
