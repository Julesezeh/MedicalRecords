from django.db import models
from Medications.models import Medication


genotypes = (
    ("aa", "AA"),
    ("as", "AS"),
    ("ss", "SS"),
    ("sc", "SC"))

blood_groups = (("a+", "A+"), ("o+", "O+"), ("b+", "B+"), ("ab+", "AB+"),
                ("a-", "A-"), ("o-", "O-"), ("b-", "B-"), ("ab-", "AB-"))
# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=144)
    last_name = models.CharField(max_length=144)
    middle_name = models.CharField(max_length=144, blank=True)
    date_of_birth = models.DateTimeField()
    allergies = models.TextField(blank=True)
    genotype = models.CharField(max_length=2, choices=genotypes)
    blood_group = models.CharField(max_length=3, choices=blood_groups)
