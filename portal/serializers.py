from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Doctor, Patient, Appointment

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['title', 'first_name', 'last_name', 'speciality' ]


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name']

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['title','description', 'created_at','date','patient','Dr']