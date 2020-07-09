__author__ = 'Carlton M'


from .models import *
from registration.models import Patient, Doctor
from django.shortcuts import render_to_response,render
from .forms import *
from .models import *
from datetime import *
from system.models import Log
import sqlite3

"""Change the hospital field of a patient"""

def index(request):
    user = request.user
    if user.first_name == "doctor":
        return render_to_response('admission_discharge/admit_discharge_main.html')
    if user.first_name == "nurse":
        return render_to_response('admission_discharge/admit_discharge_main.html')
    return render(request, 'Invalid.html')

def admit_discharge_home(request):
    user = request.user

    if user == "patient":
        return render(request,'Invalid.html')

    if user == "nurse":
        return nurse_home(request)

    if user == "doctor":
        return doctor_home(request)

    return index(request)

def nurse_home(request):
    return render(request, 'admission_discharge/admit_discharge_main.html')

def doctor_home(request):
    return render(request,'admission_discharge/admit_discharge_main.html')

def admit_patient(request):
    patient = request.POST.get('Patient')
    user = request.user
    if user.first_name == "nurse":
        if request.method == 'POST':
            form = Admission_DischargeForm(data=request.POST)
            if form.is_valid():
                form.save()
                a = Admission_Discharge.objects.all().filter(patient_id="default")[0]
                a.patient_id = patient
                a.status = "Admit"
                time = datetime.now()
                a.date_admitted = time
                #a.date_discharged = "None"
                #Log.log_action('patient transfer',request.user.email,"@"+a.hospital,'',Patient.objects.all().filter(patient_id=patient)[0].email)
                docID = Patient.objects.all().filter(patient_id=patient)[0].doctor_id
                docEmail = Doctor.objects.all().filter(doctor_id=docID)[0].email
                AdmitAlert(docEmail, Patient.objects.all().filter(patient_id=patient)[0].email)
                a.save()
                return admit_discharge_home(request)
        else:
            form = Admission_DischargeForm()

        return render(request, 'admission_discharge/admit.html',
                              {'form': form,
                               'hospital': Hospital.objects.all(),
                               'patient': Patient.objects.all()})
    if user.first_name == "doctor":
        if request.method == 'POST':
            form = Admission_DischargeForm(data=request.POST)
            if form.is_valid():
                form.save()
                a = Admission_Discharge.objects.all().filter(patient_id="default")[0]
                a.patient_id = patient
                a.status = "Admit"
                time = datetime.now()
                a.date_admitted = time
                #a.date_discharged = "None"
                #Log.log_action('patient transfer',request.user.email,"@"+a.hospital,'',Patient.objects.all().filter(patient_id=patient)[0].email)
                a.save()
                return admit_discharge_home(request)
        else:
            form = Admission_DischargeForm()

        return render(request, 'admission_discharge/admit.html',
                              {'form': form,
                               'hospital': Hospital.objects.all(),
                               'patient': Patient.objects.all()})

    return render(request, 'Invalid.html')


def select_patient(request):
    user = request.user
    if user.first_name == "doctor":
        return render(request, 'admission_discharge/select_patient.html', {'obj': Patient.objects.all()})
    if user.first_name == "nurse":
        return render(request, 'admission_discharge/select_patient.html', {'obj': Patient.objects.all()})
    else:
        return render(request, 'Invalid.html')

def patient_view(request):
    user = request.user
    if user.first_name == "doctor":
        patient = request.POST.get('Patient')
        return render_to_response('admission_discharge/patient_view.html',
                              {'obj': Admission_Discharge.objects.all().filter(patient_id=patient),
                               'patient': Patient.objects.all().filter(patient_id=patient)[0]})
    if user.first_name == "nurse":
        patient = request.POST.get('Patient')
        return render_to_response('admission_discharge/patient_view.html',
                              {'obj': Admission_Discharge.objects.all().filter(patient_id=patient),
                               'patient': Patient.objects.all().filter(patient_id=patient)[0]})
    else:
        return render(request, 'Invalid.html')

def discharge_patient(request):
    user = request.user
    if user.first_name == "doctor":
        return render(request, 'admission_discharge/select_patient_D.html', {'obj': Patient.objects.all()})
    else:
        return render(request, 'Invalid.html')

def discharge_patient2(request):
    user = request.user
    if user.first_name == "doctor":
        patientid = request.POST.get('Patient')
        patient = Patient.objects.all().filter(patient_id=patientid)[0]
        return render(request, 'admission_discharge/select_patient_D2.html',
                      {'obj': Admission_Discharge.objects.all().filter(patient_id=patientid).filter(status="Admit"),
                       'patient':patient})
    else:
        return render(request, 'Invalid.html')

def discharge_patient3(request):
    user = request.user
    if user.first_name == "doctor":
        dischargeid = request.POST.get('Discharge')
        discharge = Admission_Discharge.objects.all().filter(id=dischargeid)[0]
        time = str(datetime.now())
        discharge.date_discharged = time
        discharge.status = "Discharged"
        # Log.log_action('patient transfer',request.user.email,discharge.hospital+"@",'',Patient.objects.all().filter(patient_id=patient)[0].email)
        discharge.save()
        return render(request, 'admission_discharge/admit_discharge_main.html')
    else:
        return render(request, 'Invalid.html')


def AdmitAlert(reciever,patient):
    database = sqlite3.connect('./db.sqlite3', check_same_thread=0)  # ":memory:", check_same_thread=0)
    db = database.cursor()
    db.execute("INSERT INTO message_message (sender,receiver,subject,message,read,time) VALUES (?,?,?,?,?,?)",
               ("System",reciever,"Admit", patient + " was admitted to the hospital",0,datetime.now()))
    database.commit()
    db.close()
    database.close()