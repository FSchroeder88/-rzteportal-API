
from rest_framework import viewsets, permissions
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer
from .models import Doctor, Patient, Appointment

class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = []


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = []


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated] # Wichtig: Diese API wird nur angezeigt wenn man eingelogt ist !!!
