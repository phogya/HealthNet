from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
#from healthNet.registration.forms import PatientForm
from django.template import RequestContext
from .forms import *
from django.contrib.auth import authenticate,login,logout
from Admission_Discharge.models import Hospital
from system.models import Log
from message.models import Message
import sqlite3
import datetime



def chooseregistration(request):
    '''
    when register from the home page is click, it take you to this page where you can choose to register as a:
    -doctor
    -patient
    -nurse
    -admin
    :param request:
    :return:
    '''
    return render_to_response('chooseregistration.html')

def personal_info_reg(request):
    '''
    second page of patient registration
    :param request:
    :return:
    '''

    form = Personal_Info_Form(request.POST or None)


    if form.is_valid():
        instance = form.save(commit=False)
        #if(instance.weight_lbs < 1):
            #return render_to_response('reg1.html',{'form':form},{'invalid':True})

        form.save()
        return redirect('reg2')

    args = {}
    args.update(csrf(request))

    args['form'] = Personal_Info_Form()

    return render(request,'register.html', {"form":form},context_instance=RequestContext(request))

def med_info_reg(request):
    '''
    second page of patient registration
    :param request:
    :return:
    '''

    form = Med_Info_Form(request.POST or None)


    if form.is_valid():
        instance = form.save(commit=False)

        form.save()
        return render(request, 'patientTransfer/hospital_select.html', { 'hospitals' :Hospital.objects.all()}) #redirect to select hospital and doctor

    args = {}
    args.update(csrf(request))

    args['form'] = Med_Info_Form()

    return render(request,'register.html', {"form":form},context_instance=RequestContext(request))

def docregistration(request):
    """
    registration for non patient users, needs to be split up for doc, nurse, and admin
    :param request:
    :return:
    """

    form =DoctorForm(request.POST or None)


    if form.is_valid():
        instance = form.save(commit=False)
        if validate(instance):
            user = User.objects.create_user(instance.email, instance.email, instance.password)
            newlogin = authenticate(username=instance.email, password=instance.password)
            login(request, newlogin)
            form.save()

            p = Doctor.objects.all().filter(doctor_id="default")[0]
            p.doctor_id = user.id
            #in the auth_user type it will show that this is a patient by the first name field
            user.first_name = "doctor"
            Log.log_action('register',p.email,'','','')
            NewStaffAlert('Admin')
            p.save()
            user.save()

            return render( request, 'index.html')  ########################### I changed this

        else:
            return render_to_response('docregistration.html',{'form':form,'invalid':True},context_instance=RequestContext(request))
    args = {}
    args.update(csrf(request))

    args['form'] = DoctorForm()

    return render(request,'docregistration.html', {"form":form},context_instance=RequestContext(request))

def adminregistration(request):
    """
    registration for non patient users, needs to be split up for doc, nurse, and admin
    :param request:
    :return:
    """

    form =AdminForm(request.POST or None)


    if form.is_valid():
        instance = form.save(commit=False)
        if validate(instance):
            user = User.objects.create_user(instance.email, instance.email, instance.password)
            newlogin = authenticate(username=instance.email, password=instance.password)
            login(request, newlogin)
            form.save()
            user.first_name = "admin"
            Log.log_action('register',user.email,'','','')
            NewStaffAlert('Admin')
            user.save()

            return render( request, 'index.html')
        else:
            return render_to_response('adminregistration.html',{'form':form,'invalid':True})

    args = {}
    args.update(csrf(request))

    args['form'] = AdminForm()

    return render(request,'adminregistration.html', {"form":form},context_instance=RequestContext(request))

def validate(instance):

    if not (Patient.objects.all().filter(email=instance.email))\
            and not (Doctor.objects.all().filter(email=instance.email))\
        and not (Admin.objects.all().filter(email=instance.email))\
        and not (Nurse.objects.all().filter(email=instance.email))\
        and (len(instance.phone_number)==10) and (instance.phone_number).isdigit()\
            and instance.first_name.isalpha():
            return True
    else:
        return False
def otherregistration(request):
    """
    registration for non patient users, needs to be split up for doc, nurse, and admin
    :param request:
    :return:
    """
    z=True
    while(z):
        form =NurseForm(request.POST or None)


        if form.is_valid():
            print(form)
            instance = form.save(commit=False)
            if(validate(instance)):

                user = User.objects.create_user(instance.email, instance.email, instance.password)
                newlogin = authenticate(username=instance.email, password=instance.password)
                #login(request, newlogin)
                form.save()

                p = Nurse.objects.all().filter(nurse_id="default")[0]
                p.nurse_id = user.id
            #in the auth_user type it will show that this is a patient by the first name field
                user.first_name = "nurse"
                Log.log_action('register',p.email,'','','')
                NewStaffAlert('Admin')
                p.save()
                user.save()

                return render(request,'index.html')
                z=False

            else:
                return render_to_response('otherregistration.html',{'form':form,'invalid':True},context_instance=RequestContext(request))


        args = {}
        args.update(csrf(request))

        args['form'] = NurseForm()

        return render(request,'otherregistration.html', {"form":form})

def choose_auth(request):
    """

    :param request:
    :return:
    """
    if request.user.first_name != "admin":
        return render( request, 'Invalid.html')


    return render_to_response('authentication.html')

def auth_success(request):
    """
    allows the admin a response to reassure they added someone and allows them to choose where they
    want to go next
    :param request:
    :return:
    """
    return render_to_response('auth_success.html')

def authdoc(request):
    """

    :param request:
    :return:
    """
    p = User.objects.all().filter(is_staff=False).filter(first_name="doctor")
    print(p)
    if not p:
        return render(request, 'NoUser.html')
    user = p[0]
    user.is_staff = True
    Log.log_action('authorize',request.user.email,'','',user.email)
    user.save()
    return render_to_response('docauth.html', {'Doctor' : user})

def authadmin(request):
    """

    :param request:
    :return:
    """
    p = User.objects.all().filter(is_staff=False).filter(first_name="admin")
    if not p:
        return render(request, 'NoUser.html')
    user = p[0]
    user.is_staff = True
    Log.log_action('authorize',request.user.email,'','',user.email)
    user.save()
    return render_to_response('adminauth.html', {'Admin' : user})


def authnurse(request):
    """
    Have the patient go back in and change their info
    :param request:
    :return:
    """
    p = User.objects.all().filter(is_staff=False).filter(first_name="nurse")
    print(p)
    if not p:
        return render(request, 'NoUser.html')

    user = p[0]
    user.is_staff = True
    Log.log_action('authorize',request.user.email,'','',user.email)
    user.save()

    return render_to_response('nurseauth.html', {'Nurse' : user})


def logIn(request):
    """
    The login that takes you to the url0
    :param request:
    :return: render the page to the html login

    {% block title %}Homepage{% endblock %}
{% block content %}
    <h1><strong>HealthNet Inc.</strong></h1>
    <h3>Welcome, {{ id.get_name }}.</h3>
    """
    c ={}
    c.update(csrf(request))
    return render_to_response('login.html',c)



def auth_view(request):
    """
    authenitaction of the login in
    checks username (email) and password
    :param request:
    :return:
    """
    #if we don't get a value then we get an empty string
    #allow authenticate will still wor

    email = request.POST.get('email' )
    password = request.POST.get('password')
    #return none if not found

    user = authenticate(username=email, password=password)
    if user is not None:
            if (user.is_staff == True)or (user.first_name == 'patient'):
                auth.login(request,user)
                Log.log_action('login',email,'login','login',email)
                return redirect('dashboard')
            else:
                return render_to_response('login.html',{'noauth':True})
    else:
        err_msg = 'Please enter email and password'
        return render_to_response('login.html', {'invalid': True},context_instance=RequestContext(request))


#@login_required(login_url='/')
def dashboard(request):
    if request.method == "POST":
        if request.POST.get('delete') == "1":
            Message.objects.all().filter(sender="System").filter(receiver=request.user.email).delete()
    notifications = Message.objects.all().order_by('time').filter(sender="System").filter(receiver=request.user.email)
    if request.user.first_name == 'admin' or request.user.first_name == '':
        notifications = Message.objects.all().order_by('time').filter(sender='System').filter(receiver='Admin')
    number = len(notifications)
    return render(request,'dashboard.html',
                              {'full_name': request.user.email,"Notification":notifications,"Number":number})



def invalid_login(request):
    """
    set up a warning when a user enters the wrong qualitfications
    :param request:
    :return:
    """
    return render_to_response('invalid_login.html')

def logout(request):
    """

    :param request:
    :return:
    """
    auth.logout(request)
    return render_to_response('logout.html')




def index(request):

    form = PatientForm(request.POST or None)


    if form.is_valid():
        instance = form.save(commit=False)
        user = User.objects.create_user(instance.email, instance.email, instance.password)
        user.save()
        newlogin = authenticate(username=instance.email, password=instance.password)
        login(request, newlogin)
        form.save()
        return redirect('dashboard')

    args = {}
    args.update(csrf(request))

    args['form'] = PatientForm()

    return render(request,'register.html', {"form":form})

def registration(request):
    context  = {}
    return render(request,'registration/homepage.html', context)

def register_user(request):
    """
    Registering new user (patient)
    check the form is valid(all filled in)
    save the email as their username and password as password to login as
    :param request:
    :return:
    """
    form = PatientForm(request.POST or None)


    if form.is_valid():
        instance = form.save(commit=False)
        print((Patient.objects.all().filter(email=instance.email)))
        #validation checks, the email isnt in the system, the phone num is 10 and all num, name only contains chars
        if not (Patient.objects.all().filter(email=instance.email))\
                and (len(instance.phone_number)==10) and (instance.phone_number).isdigit()\
                and instance.first_name.isalpha():
            user = User.objects.create_user(instance.email, instance.email, instance.password)
            user.save()
            newlogin = authenticate(username=instance.email, password=instance.password)
            login(request, newlogin)
            form.save()
        else:

            return render_to_response('register.html',{'form':form,'invalid':True})
        p = Patient.objects.all().filter(patient_id="default")[0]
        p.patient_id = user.id
        #in the auth_user type it will show that this is a patient by the first name field
        user.first_name = "patient"
        p.save()
        user.save()

        return redirect('reg1')

    args = {}
    args.update(csrf(request))

    args['form'] = PatientForm()

    return render(request,'register.html', {"form":form},context_instance=RequestContext(request))

def NewStaffAlert(reciever):
    database = sqlite3.connect('./db.sqlite3', check_same_thread=0)  # ":memory:", check_same_thread=0)
    db = database.cursor()
    db.execute("INSERT INTO message_message (sender,receiver,subject,message,read,time) VALUES (?,?,?,?,?,?)",
               ("System",reciever,"New Staff","There are new staff to authorize.",0,datetime.datetime.now()))
    database.commit()
    db.close()
    database.close()
