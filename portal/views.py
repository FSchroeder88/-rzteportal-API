from django.http import HttpResponse #Wichtig muss von django.http sein
from rest_framework import viewsets, permissions
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer
from .models import Doctor, Patient, Appointment
from django.core import serializers  #Wichtig muss von django.core sein
from urllib import request


class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = []

    def create(self, request):
        doctor = Doctor.objects.create( title = request.data.get('title'),
                                        first_name = request.data.get('first_name'),
                                        last_name = request.data.get('last_name'),
                                        speciality = request.data.get('speciality'))
        serialized_obj = serializers.serialize('json', [doctor,])
        return HttpResponse(serialized_obj, content_type='application/json')


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = []

    def create(self, request):
        patient = Patient.objects.create(first_name = request.data.get('first_name'),
                                        last_name = request.data.get('last_name'))
        serialized_obj = serializers.serialize('json', [patient,])
        return HttpResponse(serialized_obj, content_type='application/json')


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    # Wichtig: Diese API wird nur angezeigt wenn man eingelogt ist !!!
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.filter(
            user__username=self.request.user.username
        )

    def create(self, request):
        appointment = Appointment.objects.create(title = request.data.get('title'),
                                                 description = request.data.get('description'),
                                                 created_at = request.data.get('created_at',''),
                                                 date = request.data.get('date', ''),
                                                 patient = request.data.get('patient'),
                                                 dr = request.data.get('dr'),
                                                 user = request.user)
        serialized_obj = serializers.serialize('json', [appointment,])
        return HttpResponse(serialized_obj, content_type='application/json')