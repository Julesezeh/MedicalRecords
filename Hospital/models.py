from django.db import models

# Create your models here.


class Hospital(models.Model):
    name = models.CharField(max_length=144)
    address = models.TextField()
    city = models.CharField(max_length=144)
    state = models.CharField(max_length=144)
    is_member = models.BooleanField(default=False)
