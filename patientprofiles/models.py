from django.db import models

# Create your models here.

# Patient
class Patient(models.Model):
  name = models.CharField()
  date_of_birth = models.DateTimeField("birthday")
  last_seen = models.DateTimeField("last appointment") 

# Ailment
class Ailment(models.Model):
  name = models.CharField()
  description = models.CharField() 

# Diagnosis
class Diagnosis(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  ailment = models.ForeignKey(Ailment, on_delete=models.CASCADE)
  date_diagnosed = models.DateTimeField("diagnosis date")

# Medication
class Medication(models.Model):
  name = models.CharField()
  description = models.CharField()

# RecommendedMed
class RecommendedMed(models.Model):
  ailment = models.ForeignKey(Ailment, on_delete=models.CASCADE)
  medication = models.ForeignKey(Medication, on_delete=models.CASCADE)

# Prescription
class Prescription(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  recommended_med = models.ForeignKey(RecommendedMed, on_delete=models.CASCADE)
  date_prescribed = models.DateTimeField("prescription date")
