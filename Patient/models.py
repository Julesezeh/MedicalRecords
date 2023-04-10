from django.db import models
from Medications.models import Medication

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=144)
    last_name = models.CharField(max_length=144)
    middle_name = models.CharField(max_length=144,blank=True)
    date_of_birth = models.DateTimeField()
    allergies = models.TextField(blank=True)
    genotype = models.Choices(['AA','AS','SS'])
    # blood_group = models.Choices(["O+","O-","AB"])
