import datetime
from email.policy import default
from django.db import models
from django.conf import settings

class Doctor(models.Model):
    ALLGEMEINMEDIZIN = 'AM'
    RADIOLOGE = 'RL'
    HAUTARZT = 'HA'
    AUGENARZT = 'AA'
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

        # def is_upperclass(self):
        #     return self.speciality in {}

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Appointment(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    created_at = models.DateField(default=datetime.date.today)
    date = models.DateTimeField()
    patient= models.ForeignKey(Patient, on_delete=models.CASCADE, default=None)
    Dr =models.ForeignKey(Doctor, on_delete=models.CASCADE, default=None)