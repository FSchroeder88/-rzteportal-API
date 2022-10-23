import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Doctor(models.Model):
    ALLGEMEINMEDIZIN = 'Allgemeinmedizin'
    RADIOLOGE = 'Radiologe'
    HAUTARZT = 'Hautarzt'
    AUGENARZT = 'Augenarzt'
    speciality_CHOICES = [
        (ALLGEMEINMEDIZIN, 'Allgemeinmedizin'),
        (RADIOLOGE, 'Radiologe'),
        (HAUTARZT, 'Hautarzt'),
        (AUGENARZT, 'Augenarzt'),
    ]

    DR = 'Dr.'
    PROF_DR = 'Prof.Dr.'
    DR_NAT = 'Dr.rer.nat.'
    title_CHOICES = [
        (DR, 'Dr.'),
        (PROF_DR, 'Prof.Dr.'),
        (DR_NAT, 'Dr.rer.nat.'),
    ]

    title = models.CharField(max_length=20, choices=title_CHOICES, default=DR)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    speciality = models.CharField(max_length=20, choices=speciality_CHOICES, default=ALLGEMEINMEDIZIN)

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Appointment(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    created_at = models.DateField(default=datetime.date.today, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    patient= models.ForeignKey(Patient, on_delete=models.CASCADE, default=None)
    dr =models.ForeignKey(Doctor, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)