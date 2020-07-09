from django.shortcuts import render
from registration.models import Patient,Personal_Info, Doctor, Nurse, Admin, Med_Info
from prescriptions.models import Prescription
from testResults.models import TestM
from django.shortcuts import render_to_response, render, redirect
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from .models import *
from django.core.context_processors import csrf
import sqlite3 as lite
import sys
from system.models import Log
from registration.models import Patient

from django.contrib.auth.models import User


def editInfos_home(request):

    user = request.user

    if user.first_name == "patient":
        return editInfos_for_patient(request)

    if user.first_name == "doctor":
        return editInfos_for_doctor(request)

    if user.first_name == "nurse":
        return editInfos_for_nurse(request)

    if user.first_name == "admin":
        return editInfos_for_admin(request)

    return render( request, 'Invalid.html')


def editInfos_for_patient(request):

    if request.user.first_name != "patient":
        return render( request, 'Invalid.html')

    userid = request.user.id
    patient = Patient.objects.all().filter(patient_id=userid)[0]

    pInfo = Personal_Info.objects.all().filter(id=patient.id)[0]


    return render(request, 'editInfos/editInfosPatient.html', { 'patient' : patient,
                                                         'pInfo' : pInfo} )

def editInfos_for_patient2(request):

    userid = request.user.id
    patient = Patient.objects.all().filter(patient_id=userid)[0]

    pInfo = Personal_Info.objects.all().filter(id=patient.id)[0]

    patient.first_name = request.POST.get('patient_first_name')
    patient.last_name = request.POST.get('patient_last_name')
    patient.phone_number = request.POST.get('patient_phone_num')
    pInfo.insurance_Number = request.POST.get('patient_insuranceNum')
    pInfo.insurance_Name = request.POST.get('patient_insuranceName')
    pInfo.name_Of_Emergency_Contact = request.POST.get('patient_ICE_Name')
    pInfo.number_Of_Emergency_Contact = request.POST.get('patient_ICE_Num')
    pInfo.marital_status = request.POST.get('patient_Marital_Status')

    Log.log_action('patient info',request.user.email,'update','',patient.email)
    pInfo.save()
    patient.save()

    return render(request, 'dashboard.html')

def editInfos_for_doctor(request):

    if request.user.first_name != "doctor":
        return render( request, 'Invalid.html')

    userid = request.user.id
    doctor = Doctor.objects.all().filter(doctor_id=userid)[0]

    return render(request, 'editInfos/editInfosDoctor.html', { 'doctor' : doctor } )

def editInfos_for_doctor2(request):

    userid = request.user.id
    doctor = Doctor.objects.all().filter(doctor_id=userid)[0]

    doctor.first_name = request.POST.get('doctor_first_name')
    doctor.last_name = request.POST.get('doctor_last_name')
    doctor.phone_number = request.POST.get('doctor_phone_num')

    Log.log_action('patient info',request.user.email,'update','',doctor.email)
    doctor.save()

    return render(request, 'dashboard.html')

def editInfos_for_admin(request):

    if request.user.first_name != "admin":
        return render( request, 'Invalid.html')

    userid = request.user.email
    admin = Admin.objects.all().filter(email=userid)[0]

    return render(request, 'editInfos/editInfosAdmin.html', { 'admin' : admin } )

def editInfos_for_admin2(request):

    userid = request.user.email
    admin = Admin.objects.all().filter(email=userid)[0]

    admin.first_name = request.POST.get('admin_first_name')
    admin.last_name = request.POST.get('admin_last_name')
    admin.phone_number = request.POST.get('admin_phone_num')

    Log.log_action('patient info',request.user.email,'update','',admin.email)
    admin.save()

    return render(request, 'dashboard.html')

def editInfos_for_nurse(request):

    if request.user.first_name != "nurse":
        return render( request, 'Invalid.html')

    userid = request.user.id
    nurse = Nurse.objects.all().filter(nurse_id=userid)[0]

    return render(request, 'editInfos/editInfosNurse.html', { 'nurse' : nurse } )

def editInfos_for_nurse2(request):

    userid = request.user.id
    nurse = Nurse.objects.all().filter(nurse_id=userid)[0]

    nurse.first_name = request.POST.get('nurse_first_name')
    nurse.last_name = request.POST.get('nurse_last_name')
    nurse.phone_number = request.POST.get('nurse_phone_num')

    Log.log_action('patient info',request.user.email,'update','',nurse.email)
    nurse.save()

    return render(request, 'dashboard.html')

def editInfos1(request):

    return render(request, 'editInfos/select_patient.html', {'obj': Patient.objects.all()})

def editInfos2(request):

    # This only gets called once, unlike forms.
    # Needs user to be done so the patient can be accessed consistently.
    # Don't know how to pass 'patient' to the next function, wont matter w/ user tho

    patient = request.POST.get('Patient')
    return render(request, 'editInfos/editInfos.html', { 'patient' : Patient.objects.all().filter(id=patient)[0]})

def editInfos3(request):

    # printed to console to confirm get
    print( request.POST.get('patient_first_name'))
    print( request.POST.get('patient_last_name'))
    print( request.POST.get('patient_email'))
    print( request.POST.get('patient_password')) # password change should probably be its own function

    # p = Patient.objects.all().filter(id=  User's id  )[0]  no way to get user yet
    # p.first_name = patient_first_name
    # p.last_name = patient_last_name
    # p.email = patient_email
    # p.password = patient_password

    return render(request, 'dashboard.html')


#################################################################
#  New UI based on Doctor House's reccomendations

def allInfo_home(request):

    if request.user:
        user = request.user
    else:
        return render( request, 'Invalid.html')

    if user.first_name == "patient":
        return patientView_patient(request)

    if user.first_name == "doctor":
        return patientSelect(request)

    if user.first_name == "nurse":
        return patientSelect(request)

    if user.first_name == "admin":
        return patientSelect(request)

def patientSelect(request):
    return render(request, 'editInfos/patientSelect.html', {'obj': Patient.objects.all()})

def patientView(request):

    patid = request.POST.get('Patient')

    patient = Patient.objects.all().filter(id=patid)[0]
    pInfo = Personal_Info.objects.all().filter(id=patid)[0]
    mInfo = Med_Info.objects.all().filter(id=patid)[0]
    user = User.objects.all().filter(id=patient.patient_id)[0]
    doctor = Doctor.objects.all().filter(doctor_id=patient.doctor_id)[0]
    urTests = TestM.objects.all().filter(patient_id=patient.patient_id).filter(viewable="Private")
    rTests = TestM.objects.all().filter(patient_id=patient.patient_id).filter(viewable="Public")
    presc = Prescription.objects.all().filter(patient_id=patient.patient_id)

    Log.log_action('patient info',request.user.email,'view','info',patient.email)

    return render_to_response('editInfos/patientView.html',
                              {'patient': patient ,
                               'doctor' : doctor,
                               'user' : user,
                               'pInfo' : pInfo,
                               'mInfo': mInfo,
                               'urTests' : urTests ,
                               'presc' : presc,
                               'rTests' : rTests })

def releaseTest(request):
    testid = request.POST.get('Test')
    test = TestM.objects.all().filter(id=testid)[0]

    test.viewable = "Public"
    test.save()

    return render( request, 'dashboard.html')

def patientView_patient(request):

    c = {}
    c.update(csrf(request))

    user = request.user

    patient = Patient.objects.all().filter(patient_id=user.id)[0]
    patid = patient.id
    pInfo = Personal_Info.objects.all().filter(id=patid)[0]
    mInfo = Med_Info.objects.all().filter(id=patid)[0]
    doctor = Doctor.objects.all().filter(id=patient.doctor_id)[0]
    urTests = TestM.objects.all().filter(patient_id=patient.patient_id).filter(viewable="Private")
    rTests = TestM.objects.all().filter(patient_id=patient.patient_id).filter(viewable="Public")
    presc = Prescription.objects.all().filter(patient_id=patient.patient_id)

    return render_to_response('editInfos/patientView_patient.html',
                              {'patient': patient ,
                               'doctor' : doctor,
                               'user' : user,
                               'pInfo' : pInfo,
                               'mInfo': mInfo,
                               'urTests' : urTests ,
                               'presc' : presc,
                               'rTests' : rTests })


