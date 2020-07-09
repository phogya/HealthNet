from django.db import models
import datetime

"""Admission/Discharge:

    Carlton and Nathan

    Doctors and Nurses can admit a patient to the hospital for an extended
    stay (reasons could be: emergency, observation, surgery, etc.). These are
    typically unexpected visits but can result from a decision made after a
    scheduled appointment. This event is recorded by the system.

    Doctors are the only ones to approve patient discharge from the hospital.
    This event is recorded by the system.

    """

class Admission_Discharge(models.Model):
    #hospital = models.CharField(max_length=200, default="default")
    patient_id = models.CharField(max_length=200, default="default")
    #date_admitted = models.CharField(max_length=100)
    date_admitted = models.DateTimeField(null=True)
    #date_discharged = models.CharField(max_length=100)
    date_discharged = models.DateTimeField(null=True)
    reason = models.CharField(max_length=200)
    status = models.CharField(max_length=200,default="default")

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

"""
    Not sure about this might need someone's help to figure this out.
    Can this be done another way, similar to registering a patient.
    Admittance (can be only be done by doctors and nurses):
    admit(){
        Search for patient in patient list
        get medical information of new patient
        add patient to hospital list
        log to system
     }

    PatientAdmit(){
        Add id to hospital
        log to system
    }

    UpdatePatientInfo(){
        if new info added
            update the system
        then log into system
    }

    Discharge (can only be done by doctors):
    discharge(id){
        doctor selects patient
        remove patient from hospital list
    }

    appproveDischarge(){
        checks to see if discharge done by doctor
    }

    UpdatePatientInfo(){
        if new info added
            update the system
        then log into system
    }
    """