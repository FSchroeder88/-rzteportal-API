from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from portal.views import AppointmentViewSet, DoctorViewSet, PatientViewSet


router = routers.DefaultRouter()
router.register(r'doctor', DoctorViewSet)
router.register(r'patient', PatientViewSet)
router.register(r'appointment', AppointmentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
