__author__ = 'Carlton'


from django.shortcuts import render_to_response, render, redirect
from .forms import *
from .models import *
from registration.models import Patient
from system.models import Log

def index(request):
    return render_to_response('prescriptions/prescription_main.html')

def prescription_add(request):
    return render_to_response('prescriptions/prescription_added.html')

def prescription_home(request):
    user = request.user

    if user.first_name == "patient":
        return patient_home(request)

    if user.first_name == "doctor":
        return doctor_home(request)

    if user.first_name == "nurse":
        return nurse_home(request)

    return render( request, 'Invalid.html')

"""Patients, doctors, and nurses should all have different prescription pages."""

"""Patients should only show the prescripitons with their current prescriptions"""
def patient_home(request):
    userid = request.user.id
    return render_to_response('prescriptions/patient_home.html',
                              {'obj': Prescription.objects.all().filter(patient_id=userid),
                               'patient' : Patient.objects.all().filter(patient_id=userid)[0]})

"""Same as the main page."""
def doctor_home(request):
    return render(request,'prescriptions/prescription_main.html')

"""Should only show the prescriptions of the current hospital's patients?"""
def nurse_home(request):
    return select_prescription(request)

def select_prescription(request):
    return render(request, 'prescriptions/select_patient.html', {'obj': Patient.objects.all()})

def prescription_create(request):
    user = request.user
    if user.first_name == "patient":
        return render(request, 'Invalid.html')
    if user.first_name == "nurse":
        return render(request,'Invalid.html')
    if user.first_name == "doctor":
        patient = request.POST.get('Patient')
        if request.method == 'POST':
            form = PrescriptionForm(data=request.POST)
            if form.is_valid():
                """

                Variables are for logging, not creating a prescription."""
                #
                # #patient_name = form.cleaned_data['patient_name']
                # medication = form.cleaned_data['medication']
                # dosage = form.cleaned_data['dose']
                # refill = form.cleaned_data['refill']
                # Log.log_action('prescription', request.user.username, 'add', dosage + ' of ' + medication, """patient_name""")

                form.save()
                #p = Prescription.objects.all().filter(patient_id=patient)[0]
                p = Prescription.objects.all().filter(patient_id="default")[0]
                p.patient_id = patient
                Log.log_action('prescription', request.user.username, 'add', p.dose + ' of ' + p.medication, Patient.objects.all().filter(patient_id=patient)[0].email)
                p.save()
                return prescription_home(request)
        else:

            """args = {}
            args.update(csrf(request))
            args['form'] = PrescriptionForm()"""
            form = PrescriptionForm()

            return render(request, 'prescriptions/prescription_create.html', {'form': form, 'obj': Patient.objects.all()})
    else:
        return render(request,'Invalid.html')


def prescription_view(request):

    patient = request.POST.get('Patient')
    """The variables and for loop are for logging, not viewing the prescriptions."""
    print(patient)
    usertype = request.user
    actualusertype = usertype.first_name #patient or nurse or admin or doctor
    userid = request.user.id
    info = ''
    # for item in Prescription.objects.all():
    #     info += item.refill + ' refills of ' + item.dose + ' of ' + item.medication + ' and '
    Log.log_action('prescription',request.user.username, 'view', info[:-5], Patient.objects.all().filter(patient_id=patient)[0].email)

    return render_to_response('prescriptions/prescription_view.html',
                              {'obj': Prescription.objects.all().filter(patient_id=patient),
                               'patient': Patient.objects.all().filter(patient_id=patient)[0]})

def prescription_remove(request):
    #http://stackoverflow.com/questions/19382664/python-django-delete-current-object
    patient = request.POST.get('Patient')
    print(Patient.objects.all().filter(patient_id=patient))
    return render(request,'prescriptions/prescription_remove.html',
                            {'obj': Prescription.objects.all()})

def prescription_removed(request):
    presc = request.POST.get('Prescription')
    rx = Prescription.objects.filter(id=presc)[0]
    # TODO: Check to make sure this gets the correct user when Carlton fixes default patient ID.
    Log.log_action('prescription',request.user.username,'remove',rx.medication,Patient.objects.all().filter(patient_id=rx.patient_id)[0].email)
    rx.delete()
    return render(request, 'prescriptions/prescription_main.html')

def select_prescription(request):
    user = request.user
    if user.first_name == "nurse":
        return render(request, 'prescriptions/select_prescription.html', {'obj': Patient.objects.all()})
    if user.first_name == "doctor":
        return render(request, 'prescriptions/select_prescription.html', {'obj': Patient.objects.all()})

    return render(request, 'Invalid.html')

def prescription_edit(request):
    return render(request, 'prescriptions/prescription_edit.html',{'obj': Prescription.objects.all()})

def prescription_edited(request):
    presc = request.POST.get('Prescription')
    rx = Prescription.objects.filter(id = presc)[0]
    rx.delete()
    return render(request,'prescriptions/prescription_edited.html',{'obj':rx})

def prescription_save(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():

            #patient_id = form.cleaned_data['patient_id']
            medication = form.cleaned_data['medication']
            dosage = form.cleaned_data['dose']
            refill = form.cleaned_data['refill']

            form.save()
    return render(request, 'prescriptions/prescription_main.html')

def prescription(request):
    context = {}
    return render(request,'prescriptions', context)
