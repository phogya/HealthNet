__author__ = 'Carlton'

import datetime
from django.db import models
import sqlite3
import logging
from . import *


class PrescriptionManager(models.Manager):
    def create_Prescription(self,patient_id,medication, pat_dob, date_issued ):
        p = self.create(patient_id=patient_id, medication=medication, pat_dob=pat_dob, date_issued=date_issued)
        return p
    def get(self):
        return id
""" Make the prescription class with a:
    Patient Name: CharField
    Patent Medication: CharField
    Patient DOB: DateField
    Date issued: DateField using auto_now_add
 """
class Prescription(models.Model):
    #patient_name = models.CharField(max_length = 200)
    patient_id = models.CharField(max_length=200,default="default")
    medication = models.CharField(max_length=200)
    dose = models.CharField(max_length=200)
    refill = models.CharField(max_length=200)
    #pat_dob = models.DateField('Patient Date of Birth')
    #date_issued = models.DateField('Date issued', auto_created=True)

    objects = PrescriptionManager()

    def __str__(self):
        #dateissued = self.date_issued.__str__()
        #patDOB = self.pat_dob.__str__()
        return "Patient Name: "+self.patient_id+" Medication: "+self.medication+" Dose: "\
               +self.dose+" Refill: "+self.refill

    def __repr__(self):
        return ("Name: {0}, Medication: {1}, Dose: {2}, Refill:{3}".format(
            self.patient_id, self.medication, self.dose, self.refill))

    """view(id): allow patients, doctors, and nurses to view the prescription
            get prescription based on id
            print(prescription object)"""
    def view(self):

        database = sqlite3.connect('./db.sqlite3', check_same_thread=0)  # ":memory:", check_same_thread=0)
        db = database.cursor()
        db.execute("select patient_name,medication,dose,refill from prescriptions_prescription")
        prescription = []
        prescription = db.fetchall()
        return prescription


    """add(id): allow doctors to add prescriptions for their patients.
        selct user user associated with prescription
        input selected prescription info"""
    def add(self):
        """return {
            'name': self.patient_name,
            'medication': self.medication,
            'pat_DOB': self.pat_DOB,
            'date_issued': self.date_issued,
                }
                """
        self.save()


    """remove(): allow doctors to remove prescriptions
            delete prescription object from associated id"""
    def remove(self):
        database = sqlite3.connect('./db.sqlite3', check_same_thread=0)
        db = database.cursor()
        db.execute("delete from Prescription_prescription where self")



#Rx = Prescription.objects.create_Prescription("John Doe", "Ibuprofen", "1969-10-03", "2015-10-03")
#Rx.save()

