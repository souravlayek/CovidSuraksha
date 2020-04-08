from django.contrib import admin
from .models import Patient,PatientInfo
# Register your models here.
admin.site.register(Patient)
admin.site.register(PatientInfo)