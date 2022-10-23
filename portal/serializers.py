from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Doctor, Patient, Appointment

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','title', 'first_name', 'last_name', 'speciality' ]


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ['id','first_name', 'last_name']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Appointment
        fields = ['id','title','description', 'created_at','date','patient','dr','user']