from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# I need a patient list/index thing, 
def index(request):
  return HttpResponse("Hello World!")
# I need a patient view detail thing,
# I need an ailment view detail thing (linked through patient and through medication)
# I need a medication view detail thing (linked through patient, and through medication)
# I need a bill view for the patient with list of medications only I guess?

