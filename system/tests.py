from django.test import TestCase
from .models import *
# Create your tests here.

class SystemTestCase(TestCase):
    def setUp(self):
        pass


    def test_log_output(self):
        self.assertEqual(Log.prescription('Doctor','view','budesonide','patient'),
                         "Doctor viewed patient's prescription of budesonide.")
        self.assertEqual(Log.test_results('Doctor','release','remicade','Nathan'),
                         'Doctor released remicade test results for Nathan.')
        self.assertEqual(Log.appointment('Nurse','edit','Kayla'),
                         'Nurse edited an appointment for Nathan.')
        self.assertEqual(Log.unknown('asdf','asdf','asdf','asdf','asdf'),
                         'An unknown event involving asdf, asdf, asdf, asdf, and asdf has occurred.')
        self.assertEqual(Log.patient_info('Patient', 'update','patient'),
                         "Patient updated patient's patient information")
        self.assertEqual(Log.patient_transfer('Patient','Strong Memorial','Rochester General'),
                         'Patient was transferred from Strong Memorial to Rochester General.')