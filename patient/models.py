from django.db import models
from django.db import models

class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(unique=True)

    glucose = models.FloatField()
    haemoglobin = models.FloatField()
    cholesterol = models.FloatField()

    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.full_name
