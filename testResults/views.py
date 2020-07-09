from django.shortcuts import render_to_response, render, redirect
from .models import *
from django.core.context_processors import csrf
import sqlite3 as lite
import sys
from system.models import Log
from registration.models import Patient



def test_home(request):

    if request.user:
        user = request.user
    else:
        return render( request, 'Invalid.html')

    if user.first_name == "patient":
        return patient_test_home(request)

    if user.first_name == "doctor":
        return doctor_test_home(request)

    if user.first_name == "nurse":
        return nurse_test_home(request)

    if user.first_name == "admin":
        return nurse_test_home()

    #return render(request, 'testResults/select_patient_to_add.html', {'obj': Patient.objects.all()})
    #return render(request, 'testResults/select_patient.html', {'obj': Patient.objects.all()})

# similar to patient, needs a way to get doctor's unique identifier to filter their patients
# current version lists all patients
def doctor_test_home(request):
    return render( request, 'testResults/test_home.html')


def nurse_test_home(request):
    return select_patient(request)


# needs a way to get users insurance num to filter tests
# use login required and user parameter?
def patient_test_home(request):

    userid = request.user.id

    return render_to_response('testResults/view_test_for_patient.html',
                              {'tests': TestM.objects.all().filter(patient_id=userid).filter(viewable="Public") ,
                               'patient' : Patient.objects.all().filter(patient_id=userid)[0]})

def select_patient(request):
    return render(request, 'testResults/select_patient.html', {'obj': Patient.objects.all()})

def select_patient_to_add(request):
    return render(request, 'testResults/select_patient_to_add.html', {'obj': Patient.objects.all()})


def view_test(request):
    """
    Variables and for loop are for logging, not viewing tests.
    """

    patient = request.POST.get('Patient')

    info = ''
    pat = str(Patient.objects.all().filter(patient_id=patient)[0])
    for item in TestM.objects.all().filter(patient_id=patient):
        info += (str(item.test_name) + ", and ")
    Log.log_action('test results', request.user.username, 'view', info[:-6], pat)

    return render_to_response('testResults/view_test2.html',
                              {'tests': TestM.objects.all().filter(patient_id=patient) ,
                               'patient' : Patient.objects.all().filter(patient_id=patient)[0]})

def add_test(request):

    patient = request.POST.get('Patient')
    viewable = request.POST.get('Viewable')
    #image = request.POST.get('file_name')

    if request.method == 'POST':
        form = TestMF(data=request.POST)

        if form.is_valid():

            form.save()

            p = TestM.objects.all().filter(patient_id="default")[0]
            p.patient_id = patient
            p.viewable = viewable
            #p.image = image

            """
            Logging
            """
            pat = str(Patient.objects.all().filter(patient_id=patient)[0])
            Log.log_action('test results', request.user.username, 'upload',p.test_name , pat)

            p.save()

            return test_home(request)
    else:
        form = TestMF()

    return render(request, 'testResults/add_test2.html', {'form': form,'obj': Patient.objects.all()})

def change_viewable1(request):
    return render(request, 'testResults/select_patient_V.html', {'obj': Patient.objects.all()})

def change_viewable2(request):
    patientid = request.POST.get('Patient')
    patient = Patient.objects.all().filter(patient_id=patientid)[0]
    return render(request, 'testResults/select_test_V.html', {'obj': TestM.objects.all().filter(patient_id=patientid).filter(viewable="Private"),
                                                              'patient': patient})

def change_viewable3(request):
    testid = request.POST.get('Test')
    test = TestM.objects.all().filter(id=testid)[0]

    test.viewable = "Public"
    Log.log_action('test results', request.user.username, 'release',test.test_name , Patient.objects.all().filter(patient_id=test.patient_id)[0].email)
    test.save()

    return test_home(request)  ################################## Dashboard not rendering correctly.

def edit_infos_test1(request):

    return render(request, 'testResults/select_patient_infos_test.html', {'obj': Patient.objects.all()})

def edit_infos_test2(request):

    # This only gets called once, unlike forms.
    # Needs user to be done so the patient can be accessed consistently.
    # Don't know how to pass 'patient' to the next function, wont matter w/ user

    patient = request.POST.get('Patient')
    return render(request, 'testResults/edit_infos.html', { 'patient' : Patient.objects.all().filter(patient_id=patient)[0]})


def delete_test1(request):

    return render(request, 'testResults/delete_test1.html', { 'obj' : TestM.objects.all()})

def delete_test2(request):

    testid = request.POST.get('Test')

    test = TestM.objects.all().filter(id=testid)[0]

    pat = str(Patient.objects.all().filter(patient_id=test.patient_id)[0])
    Log.log_action('test',request.user,'delete',test.test_name,pat)

    test.delete()

    return render( request, 'dashboard.html')