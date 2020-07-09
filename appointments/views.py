from django.shortcuts import render_to_response, render, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from .forms import *
import logging
from system.models import Log

#logger = logging.getLogger(__name__)
# Create your views here.
def appointment_form(request):
    '''

    :param request:
    :return:
    '''

    form = AppointmentForm(request.POST or None)
    print("About to check validity")

    if form.is_valid():
        print("This form is valid.")
        instance = form.save(commit=False)

        """
        Logging
        """
        title=form.cleaned_data["title"]
        description = form.cleaned_data["description"]
        #location = form.cleaned_data["location"]   this was not in fields so I was unsure how this was going to work in or if it needed to be -Mel
        start_time = form.cleaned_data["start_time"]
        end_time = form.cleaned_data["end_time"]

        Log.log_action('appointment',request.user.username,'create',description,request.user.id)

        instance.save()
        return redirect('calendar')
    print("Form is not valid.")
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(request, 'calendar.html', args)



