from django.test import TestCase
from .models import Prescription

class PrescriptionTestCase(TestCase):
    def setUp(self):
        Prescription.objects.create(patient_id="John", medication="love")

    def test_Prescription(self):
        john = Prescription.objects.get(patient_id="John")


