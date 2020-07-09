__author__ = 'Nathan'
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
"""
Points to html file for the page
"""

def statistics(request):
    if request.user.first_name != "" and request.user.first_name != "admin":  # In auth_user table, first name atrribute is left
                                        # as an empty string but filled in for all other types of accounts.
        return render( request, 'Invalid.html')
    context = {"num_user":Stats.num_user(),"num_patients":Stats.num_patients(),"num_doctor":Stats.num_doctors(),"num_admin":Stats.num_admin(),"num_admit": Stats.num_admit(),"num_nurse":Stats.num_nurse(),"num_visits":Stats.num_visits(),"visit_length":Stats.visit_length(),"admission":Stats.admission_reason(),"prescriptions":Stats.prescription_stats()}
    return render(request, 'system/stats.html', context)

def log(request):  # View the entire log.

    """if request.user.first_name != "" and request.user.first_name != "admin":  # In auth_user table, first name atrribute is left
                                        # as an empty string but filled in for all other types of accounts.
       return render( request, 'Invalid.html')

    Reads the log file, outputs it onto the website.
    :param request:
    :return:
    """
    user=[]
    action=[]
    context = {"logentry": Log.read_log,"user":Log.objects.values('user').distinct(), "action":Log.objects.values('trigger').distinct()}
    return render(request, 'system/log.html', context)


def logfilter(request):  # view log filtered based upon username and/or action.
    if request.user.first_name != "" and request.user.first_name != "admin":  # In auth_user table, first name atrribute is left
                                        # as an empty string but filled in for all other types of accounts.
       return render(request, 'Invalid.html')

    log = Log.read_log()
    action = request.POST.get('LoggingActions')  # name="LoggingActions" (from html)
    user = request.POST.get('Usernames') # name="Usernames" (from html)
    if action == "None" and user == "None":  # Because they both take on a none object,
                                            # it is assumed that the log is not being filtered.
                                            # will change what it checks for when I add a default value.
        context = {"logentry": log}
    elif action == "None":  # Filter for user only
        context = {"logentry": log.filter(user=user)}  # user is the name of the column in the log table.
    elif user == "None":  # Filter for action only
        context = {"logentry": log.filter(trigger=action)}  # trigger is the name of the column in the log table.
    else:  # Filter for both action and user
        context = {"logentry": log.filter(user=user).filter(trigger=action)}
    return render(request, 'system/logfilter.html',context)