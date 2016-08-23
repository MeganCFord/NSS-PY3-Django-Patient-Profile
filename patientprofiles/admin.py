from django.contrib import admin

from .models import Patient, Ailment, Medication

# Register your models here.
admin.site.register(Ailment)
admin.site.register(Medication)
admin.site.register(Patient)



