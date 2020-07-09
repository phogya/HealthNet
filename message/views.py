from itertools import chain
from django.shortcuts import render, redirect
from .models import *
from registration.models import Doctor, Nurse, Admin
import sqlite3
import datetime
from system.models import Log

# Create your views here.

def sendNew(request):
    if str(request.user) == "AnonymousUser":
        return render(request, 'Invalid.html')
    receiver = request.POST.get('Receiver')
    sender = request.user.email

    if request.method == 'POST':
        form = MessageForm(data=request.POST)

        if form.is_valid():
            if receiver == "None":
                context = {"obj": list(chain(Doctor.objects.all(), Nurse.objects.all())), "form": form,
                           "sendfailed": True}
                return render(request, 'message/sendNew.html', context)

            form.save()

            m = Message.objects.all().order_by('time').reverse()[0]  # Newest message.
            m.sender = sender
            m.receiver = receiver
            m.save()
            NewMessageAlert(receiver)

            """
            Logging?
            """
            # pat = str(Patient.objects.all().filter(patient_id=patient)[0])
            # TODO: Logging for messaging?
            Log.log_action('message', request.user.username, '','', receiver)

            #p.save()
            return redirect('inbox')
        return redirect('sendNew')
    else:
        form = MessageForm()
        sendTo = list(chain(Doctor.objects.all(), Nurse.objects.all()))
        return render(request, 'message/sendNew.html', {'form': form, 'obj': sendTo})


def inbox(request):
    if str(request.user) == "AnonymousUser":
        return render(request, 'Invalid.html')
    if request.method =="POST":

        #Deleting Messages
        if request.POST.get('delete') == "1":
            timeString = request.POST.get('time')

            # Make the time string editable.
            # Breaks down string to ["<Month Abrv>.", "<date>,", "<year>,", "<time>", "<a.m. or p.m.>"]
            timeArray = timeString.split()

            # replace "a.m." with "AM" or "p.m." with "PM" so strptime() parses correctly.
            if timeArray[4] == "a.m.":
                timeArray[4] = "AM"
            else:
                timeArray[4] = "PM"

            # Reconstruct string to be made into datetime object.
            timeString = str(timeArray[0]+ " " +timeArray[1]+ " " +timeArray[2]+ " " +timeArray[3]+ " " +timeArray[4])

            # Create a datetime object that is to the whole minute before the message was sent.
            time1 = datetime.datetime.strptime(timeString, '%b. %d, %Y, %I:%M %p')

            # Change timeString to the minute after the message was sent.
            time2Array=timeString.split(':')
            time2Array[1]=str(int(time2Array[1][0:2])+1)+time2Array[1][2:]
            time2String = time2Array[0]+":"+time2Array[1]

            # Create a datetime object that is to the whole minute after the message was sent.
            time2=datetime.datetime.strptime(time2String,'%b. %d, %Y, %I:%M %p')

            # Get other deleting message information.
            sender = request.POST.get('sender')
            receiver = request.POST.get('receiver')
            message = request.POST.get('message')
            subject = request.POST.get('subject')

            # filter messages against sender, reciever, time range, subject, and message.
            m = Message.objects.all().filter(time__gt=time1).filter(time__lt=time2).filter(sender=sender).filter(receiver=receiver)\
                .filter(message=message).filter(subject=subject)

            m.delete()
    context = {'Messages': Message.objects.all().order_by('time').reverse().filter(receiver=request.user.email).exclude(sender='System'),
               'coworker': list(chain(Doctor.objects.all(), Nurse.objects.all(),Admin.objects.all()))}
    return render(request, 'message/inbox.html', context)


def sentBox(request):
    if str(request.user) == "AnonymousUser":
        return render(request, 'Invalid.html')
    context = {'Messages': Message.objects.all().order_by('time').reverse().filter(sender=request.user.email),
               'coworker': list(chain(Doctor.objects.all(), Nurse.objects.all(),Admin.objects.all()))}
    return render(request, 'message/sentBox.html', context)


def reply(request):
    if str(request.user) == "AnonymousUser":
        return render(request, 'Invalid.html')
    prevMessage = request.POST.get('message')  # Previous Message contents
    email = request.POST.get('ReplyTo')  # Who sent the message
    subject = request.POST.get('subject')  # Messages subject
    time = request.POST.get('time')  # time message was sent
    receiver = request.POST.get('receiver')

    # Clicked Delete button under the desired message.
    if 'Delete' in request.POST:
        context={'receiver':receiver,"time":time,'subject':subject,'sender':email,'message':prevMessage}
        return render(request,'message/delete.html',context)

    # Clicked Reply button under desired message.
    else:
        form = MessageForm(initial={'subject':"RE: "+subject})
        sendTo = list(chain(Doctor.objects.all().filter(email=email), Nurse.objects.all().filter(email=email),
                        Admin.objects.all().filter(email=email)))
        context = {"form": form,"obj":sendTo,'prevMes':prevMessage,'prevSub':subject}
        return render(request, 'message/reply.html', context)

def NewMessageAlert(reciever):
    database = sqlite3.connect('./db.sqlite3', check_same_thread=0)  # ":memory:", check_same_thread=0)
    db = database.cursor()
    db.execute("INSERT INTO message_message (sender,receiver,subject,message,read,time) VALUES (?,?,?,?,?,?)",
               ("System",reciever,"New Message","You have a new message",0,datetime.datetime.now()))
    database.commit()
    db.close()
    database.close()

def deleteMessage(request):
    message = request.POST.get('message')
    subject = request.POST.get('subject')
    sender = request.POST.get('ReplyTo')
    receiver = request.POST.get('receiver')
    time = request.POST.get('time')
    context = {'message':message,'time':time,'subject':subject,'sender':sender,'receiver':receiver}
    return render(request,'message/delete.html',context)