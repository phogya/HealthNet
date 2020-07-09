import csv
from registration.models import Patient, Personal_Info
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from system.models import Log


def privacyCheck(request):
    user = request.user

    if user.first_name == "patient":
        return render( request, 'impexpInfo/privacy.html')

    return render( request, 'impexpInfo/invalidUser.html')

def declineCheck(request):

    return render( request, 'dashboard.html')


def export(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="YourInfo.csv"'

    user = request.user

    patient = Patient.objects.all().filter(patient_id=user.id)[0]
    pInfo = Personal_Info.objects.all().filter(id=patient.id)[0]

    writer = csv.writer(response)

    writer.writerow([user.first_name,user.email,patient.password,patient.first_name,patient.last_name,patient.hospital,
                     pInfo.name_Of_Emergency_Contact,pInfo.number_Of_Emergency_Contact,"nil"])
    Log.log_action('ImpExp',request.user.email,'Exp','','')
    return response


def get_file_name(request):

    user = request.user

    if user.first_name != "admin":
        return render( request, 'invalid.html')

    return render(request, 'impexpInfo/get_file_name.html')

def importCSV(request):

    path = request.POST.get('file_name')

    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            user = User.objects.create_user(email=row[1], username=row[1], first_name=row[0], password=row[2])
            patient = Patient.objects.create(first_name=row[3],last_name=row[4],hospital=row[5],
                                             email=row[1], password=row[2], phone_number="None")
            pInfo = Personal_Info.objects.create(insurance_Number=row[7], insurance_Name=row[6], name_Of_Emergency_Contact="None",
                                                 number_Of_Emergency_Contact="None",sex="None",weight_lbs=0,height_inches=0,marital_status="None")
            pInfo.save()
            patient.personal_info = pInfo
            patient.save()
            user.save()
    Log.log_action('ImpExp',request.user.email,'Imp','','')
    return render( request, 'dashboard.html')