from django.conf.urls import url
from . import views

urlpatterns = [
  #ok, so index is going to show a list of all the patients. the patient names will be links to view their detail.
  url(r"^$", views.index, name="index"),
  # ex: /patientprofiles/patient/2/
  url(r'^patient/(?P<patient_id>[0-9]+)/$', views.patient, name='patient'),
    # ex: /patientprofiles/ailment/1/
  url(r'^ailment/(?P<ailment_id>[0-9]+)/$', views.ailment, name='ailment'),
    # ex: /patientprofiles/medication/1/
  url(r'^medication/(?P<medication_id>[0-9]+)/$', views.medication, name='medication'),
]
