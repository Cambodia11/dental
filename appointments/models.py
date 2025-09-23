from django.db import models
from django.forms.fields import DateField, DateTimeField
from datetime import datetime

from patients.models import Patient
from doctor.models import Doctor

class Appointments(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient} Записан к {self.doctor} на {self.date}"

