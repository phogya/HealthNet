from django.shortcuts import render_to_response, render, redirect
from .models import *
from django.core.context_processors import csrf
import sqlite3 as lite
import sys
from system.models import Log
from registration.models import Patient, Doctor
from Admission_Discharge.models import Hospital
from calendar import HTMLCalendar
from datetime import date
from itertools import groupby
from django.utils.html import conditional_escape as esc
from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe

from django.shortcuts import render_to_response, render, redirect
from .models import *
from django.core.context_processors import csrf
import sqlite3 as lite
import sys
from system.models import Log
from registration.models import Patient, Doctor
from Admission_Discharge.models import Hospital

def add_appt_home(request):

    if request.user:
        user = request.user
    else:
        return render( request, 'Invalid.html')

    if user.first_name == "patient":
        return add_appt_patient(request)

    if user.first_name == "doctor":
        return add_appt_doctor(request)

    if user.first_name == "nurse":
        return add_appt_nurse(request)

    if user.first_name == "admin":
        return add_appt_nurse(request)

def add_appt_patient(request):

    user = request.user
    patient = Patient.objects.all().filter(patient_id=user.id)[0]

    year = request.POST.get('year')
    month = request.POST.get('month')
    day = request.POST.get('day')
    start_time_hour = request.POST.get('start_time_hour')
    start_time_min = request.POST.get('start_time_min')
    start_time_apm = request.POST.get('start_time_apm')
    end_time_hour = request.POST.get('end_time_hour')
    end_time_min = request.POST.get('end_time_min')
    end_time_apm = request.POST.get('end_time_apm')
    hospital = request.POST.get('hospital')



    if request.method == 'POST':
        form = ApptForm(data=request.POST)

        if form.is_valid():


            form.save()
            a = Appt.objects.all().filter(patient="default")[0]
            h = Hospital.objects.all().filter(id=hospital)[0]
            a.doctor = patient.doctor_id
            a.patient = user.id ####
            a.year = year
            a.month = month
            a.day = day
            a.start_time_hour = start_time_hour
            a.start_time_min = start_time_min
            a.start_time_apm = start_time_apm
            a.end_time_hour = end_time_hour
            a.end_time_min = end_time_min
            a.end_time_apm = end_time_apm
            a.hospital = h.name

            a.save()
            return redirect('dashboard')
    else:
        form = ApptForm()

    return render(request, 'calendar2/add_appt_patient.html', {'form': form,
                                                       'hospitals': Hospital.objects.all(),
                                                       })

def add_appt_doctor(request):

    user = request.user

    patient = request.POST.get('Patient')
    doctor = Doctor.objects.all().filter(doctor_id=user.id)[0]
    year = request.POST.get('year')
    month = request.POST.get('month')
    day = request.POST.get('day')
    start_time_hour = request.POST.get('start_time_hour')
    start_time_min = request.POST.get('start_time_min')
    start_time_apm = request.POST.get('start_time_apm')
    end_time_hour = request.POST.get('end_time_hour')
    end_time_min = request.POST.get('end_time_min')
    end_time_apm = request.POST.get('end_time_apm')
    hospital = request.POST.get('hospital')



    if request.method == 'POST':
        form = ApptForm(data=request.POST)

        if form.is_valid():


            form.save()
            a = Appt.objects.all().filter(patient="default")[0]
            h = Hospital.objects.all().filter(id=hospital)[0]
            a.doctor =  doctor.id
            a.patient = patient
            a.year = year
            a.month = month
            a.day = day
            a.start_time_hour = start_time_hour
            a.start_time_min = start_time_min
            a.start_time_apm = start_time_apm
            a.end_time_hour = end_time_hour
            a.end_time_min = end_time_min
            a.end_time_apm = end_time_apm
            a.hospital = h.name

            a.save()
            return redirect('dashboard')
    else:
        form = ApptForm()

    return render(request, 'calendar2/add_appt_doctor.html', {'form': form,
                                                       'hospitals': Hospital.objects.all(),
                                                       'patients': Patient.objects.all(),
                                                       })


def add_appt_nurse(request):
    patient = request.POST.get('Patient')
    doctor = request.POST.get('Doctor')
    year = request.POST.get('year')
    month = request.POST.get('month')
    day = request.POST.get('day')
    start_time_hour = request.POST.get('start_time_hour')
    start_time_min = request.POST.get('start_time_min')
    start_time_apm = request.POST.get('start_time_apm')
    end_time_hour = request.POST.get('end_time_hour')
    end_time_min = request.POST.get('end_time_min')
    end_time_apm = request.POST.get('end_time_apm')
    hospital = request.POST.get('hospital')



    if request.method == 'POST':
        form = ApptForm(data=request.POST)

        if form.is_valid():


            form.save()
            a = Appt.objects.all().filter(patient="default")[0]
            h = Hospital.objects.all().filter(id=hospital)[0]
            a.doctor = doctor
            a.patient = patient
            a.year = year
            a.month = month
            a.day = day
            a.start_time_hour = start_time_hour
            a.start_time_min = start_time_min
            a.start_time_apm = start_time_apm
            a.end_time_hour = end_time_hour
            a.end_time_min = end_time_min
            a.end_time_apm = end_time_apm
            a.hospital = h.name

            a.save()
            return redirect('dashboard')
    else:
        form = ApptForm()

    return render(request, 'calendar2/add_appt_nurse.html', {'form': form,
                                                       'hospitals': Hospital.objects.all(),
                                                       'patients': Patient.objects.all(),
                                                       'doctors': Doctor.objects.all()
                                                       })

def view_cal(request):
    """
    views the calander view of all appointments in a weekly view
    :param request:
    :return:
    """
    return calendar(request, 2015, 12)

    return render(request,'calendar2/view_cal.html')


def calendar(request, year, month):
    my_appts = Appt.objects.all().filter(
    month=month, year=year
    )#year also needs to be filtered, add an order by

    cal = Calendar(my_appts).formatmonth(year, month)

    return render(request,'calendar2/view_cal.html', {'calendar': mark_safe(cal),})

def choose_appt(request):

    return render(request, 'calendar2/choose_appt.html')

def view_appt(request):
    """
    viewing the appts on a certain day
    :param request:
    :return:
    """
    day=request.POST.get('day')
    month = request.POST.get('month')
    year=request.POST.get('year')
    appt = Appt.objects.all().filter(
        month=month, day=day, year=year
    )

    if len(appt)==0:
        print("lll")
        return render(request,'calendar2/view_cal.html',{'invalid':True})
    if len(appt)==1:
        print(appt)
        title=appt[0].title
        description = appt[0].description
        return render(request,'calendar2/view_appt.html',{'appt':appt[0]})
    if len(appt)>1:
        return render(request, 'calendar2/choose_appt.html')
    return render(request,'calendar2/view_appt.html',{'day':day,
                                                      'month':month,
                                                      'year':year} )





class Calendar(HTMLCalendar):

    def __init__(self, appts):
        super(Calendar, self).__init__()
        self.appts = self.group_by_day(appts)
        print(self.appts)
    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if str(day) in self.appts:
                cssclass += ' filled'
                body = ['<ul>']
                print(self.appts[str(day)])
                for appt in self.appts[str(day)]:
                    print("l")
                    body.append('<li>')
                    #body.append('<a href="%s">'% appt.get_absolute_url())
                    body.append(esc(appt.title))
                    body.append('</a></li>')
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(Calendar, self).formatmonth(year, month)

    def group_by_day(self, appts):
        field = lambda appts: appts.day
        return dict(
            [(day, list(items)) for day, items in groupby(appts, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)



"""
    Attempt of absolute url
    for appt in self.appts[str(day)]:
                    print("l")
                    body.append('<li>')
                    body.append('<a href="%s">'% appt.get_absolute_url())
                    body.append(esc(appt.title))
                    body.append('</a></li>')
                body.append('</ul>')


"""