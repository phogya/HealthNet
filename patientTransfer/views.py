from django.shortcuts import render_to_response, render, redirect
from registration.models import Patient, Doctor
from Admission_Discharge.models import Hospital
from system.models import Log
import sqlite3
import datetime


def transfer_home(request):

    userType = request.user.first_name

    if userType == "patient":
        return render( request, 'invalid.html')

    return render(request, 'patientTransfer/transfer_select.html', {'patients': Patient.objects.all(),
                                                                    'hospitals': Hospital.objects.all()})

def do_transfer(request):

    patient = request.POST.get('Patient')
    hospital = request.POST.get('Hospital')

    p = Patient.objects.all().filter(id=patient)[0]
    h = Hospital.objects.all().filter(id=hospital)[0]


    #if p.hospital == hospital:
        #render a failure state, patients hospital is not being changed


    print(h.name)
    Log.log_action('patient transfer',request.user.email,str(p.hospital)+"@"+str(h.name),'info',p.email)
    p.hospital = h.name
    p.save()
    docEmail = Doctor.objects.all().filter(id=p.doctor_id)[0].email
    TransferAlert(docEmail,p.email,h.name)
    TransferAlert(p.email, p.email, h.name)

    return redirect('dashboard')

def hospital_select(request):

    return render(request, 'patientTransfer/hospital_select.html', { 'hospitals' : Hospital.objects.all()})


def do_initial_transfer(request):

    userid = None
    if request.user.is_authenticated():
        userid = request.user.id
    #else:
        #redirect to login page

    hosp = request.POST.get('Hospital')
    print(hosp)

    p = Patient.objects.all().filter(patient_id=userid)[0]
    h = Hospital.objects.all().filter(id=hosp)[0]
    p.hospital = h.name
    p.save()

    return render(request, 'patientTransfer/doctor_select.html', { 'doctors' :Doctor.objects.all() } )

def doctor_select(request):

    return render(request, 'patientTransfer/doctor_select.html', { 'doctors' : Doctor.objects.all()})

def do_doctor_select(request):

    userid = None
    if request.user.is_authenticated():
        userid = request.user.id
    #else:
        #redirect to login page

    p = Patient.objects.all().filter(patient_id=userid)[0]
    p.doctor_id = request.POST.get('Doctor')
    p.save()

    return redirect('dashboard')

def TransferAlert(reciever,patient,hospital):
    database = sqlite3.connect('./db.sqlite3', check_same_thread=0)  # ":memory:", check_same_thread=0)
    db = database.cursor()
    db.execute("INSERT INTO message_message (sender,receiver,subject,message,read,time) VALUES (?,?,?,?,?,?)",
               ("System",reciever,"Transfer", patient + " was transfered to " + hospital,0,datetime.datetime.now()))
    database.commit()
    db.close()
    database.close()