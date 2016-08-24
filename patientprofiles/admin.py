from django.contrib import admin

from .models import Patient, Ailment, Medication, PatientAilment, PatientAilmentMedication

# Register your models here.
admin.site.register(Ailment)
admin.site.register(Medication)
admin.site.register(Patient)
admin.site.register(PatientAilment)
admin.site.register(PatientAilmentMedication)



