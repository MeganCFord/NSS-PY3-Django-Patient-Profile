from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# Patient
class Patient(models.Model):
  name = models.CharField(max_length=200)
  birthday = models.DateField("birthday")
  last_seen = models.DateTimeField("last appointment") 
  def __str__(self):
    return self.name

# Ailment
class Ailment(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=2000)
  def __str__(self):
    return self.name

# Medication
class Medication(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=2000)
  def __str__(self):
    return (self.name)

# Join table 1
class PatientAilment(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  ailment = models.ForeignKey(Ailment, on_delete=models.CASCADE)
  date_diagnosed = models.DateField("diagnosis date")

# Join table 2
class PatientAilmentMedication(models.Model):
  patient_ailment = models.ForeignKey(PatientAilment, on_delete=models.CASCADE)
  medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
  date_prescribed = models.DateField("prescription date")
