from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Patient, Ailment, Medication

# Create your views here.

# I need a patient list/index thing, 
def index(request):
  patient_list = Patient.objects.order_by("name")
  context = {"patient_list": patient_list}
  return render(request, "patientprofiles/index.html", context)
# I need a patient view detail thing,
def patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, "patientprofiles/patient.html", {"patient": patient})
# I need an ailment view detail thing (linked through patient and through medication)
def ailment(request, ailment_id):
  return HttpResponse("view ailment here.")
# I need a medication view detail thing (linked through patient, and through medication)
def medication(request, medication_id):
  return HttpResponse("view medication here.")
