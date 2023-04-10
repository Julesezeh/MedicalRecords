from django.db import models
from Patient.models import Patient
from Hospital.models import Hospital
# Create your models here.

class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hospital  = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    date_issued = models.DateTimeField()
    prescription = models.CharField(max_length=144)
    dosage = models.CharField(max_length=144)
    is_active = models.BooleanField(default=True)