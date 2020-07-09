__author__ = 'Nathan'
"""
Functions go in this file.
"""
import logging
import sqlite3
from django.db import models
import time
import datetime

"""
Actions that are logged:

Update/View patient medical information
Patient Transfer
Patient Admission/Discharge

prescription added
prescription removed

Add/Cancel appointment

Doc Releasing test results
"""

logging.basicConfig(filename='./log.txt', level=logging.INFO, format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
database = sqlite3.connect('./db.sqlite3', check_same_thread=0)  # ":memory:", check_same_thread=0)
db = database.cursor()


class Log(models.Model):

    """
    A class that takes care of logging system activity. An over arching function is called by other modules,
    and calls helper methods to fill in the appropriate information for that activitey.
    """

    time = models.DateTimeField()
    trigger = models.CharField(max_length=10000)
    user = models.CharField(max_length=10000)
    action = models.CharField(max_length=10000)
    info = models.CharField(max_length=10000)
    patient = models.CharField(max_length=10000)
    comment = models.CharField(max_length=10000)


    @staticmethod
    def log_action(trigger,user,action,info,patient):
        """
        Writes action to log.txt
        :param trigger: the module that triggers the log.
        :param user: user triggering the log.
        :param action: the action triggering the log
        :param info: information about the action
        :param patient: the patient's name
        """
        Log.log_action_db(trigger,user,action,info,patient)
        if trigger == 'patient info':
            logging.info(Log.patient_info(user,action,patient))
        elif trigger == 'patient transfer':
            hospitals = action.split("@")
            print(hospitals)
            logging.info(Log.patient_transfer(user, patient,hospitals[0],hospitals[1]))
        elif trigger == 'prescription':
            logging.info(Log.prescription(user,action,info,patient))
        elif trigger == 'appointment':
            logging.info(Log.appointment(user,action,info,patient))
        elif trigger == 'test results':
            logging.info(Log.test_results(user,action,info,patient))
        elif trigger == 'calendar':
            logging.info(Log.calendar(user))
        elif trigger == 'register':
            logging.info(Log.register(user))
        elif trigger == 'login':
            logging.info(Log.log_in(user))
        else:
            logging.info(Log.unknown(trigger,user,action,info,patient))

    @staticmethod
    def log_action_db(trigger,user,action,info,patient):
        """
        Logs action to the database.
        :param trigger: the module that triggers the log.
        :param user: user triggering the log.
        :param action: the action triggering the log
        :param info: information about the action
        :param patient: the patient's name
        """
        comment = ''
        if trigger == 'patient info':
            comment = Log.patient_info(user,action,patient)
        elif trigger == 'patient transfer':
            hospitals = action.split("@")
            comment = Log.patient_transfer(user, patient,hospitals[0],hospitals[1])
        elif trigger == 'prescription':
            comment = Log.prescription(user,action,info,patient)
        elif trigger == 'appointment': # TODO
            comment = Log.appointment(user,action,info,patient)
        elif trigger == 'test results':
            comment = Log.test_results(user,action,info,patient)
        elif trigger == 'calendar':
            comment = Log.calendar(user)
        elif trigger == 'register':
            comment = Log.register(user)
        elif trigger == 'login':
            comment = Log.log_in(user)
        elif trigger == 'authorize':
            comment = Log.auth(user,patient)  # User that authorized, user that was authorized.
        elif trigger == 'message':
            comment = Log.message(user,patient)
        elif trigger == 'ImpExp':
            comment = Log.ImpExp(user,action)
        else:
            comment = Log.unknown(trigger,user,action,info,patient)
        add = (datetime.datetime.now(), trigger, user, action, info, patient, comment)
        db.execute('INSERT INTO system_log(time, trigger, action, info, patient, comment, user) VALUES(?,?,?,?,?,?,?)',
                   (datetime.datetime.now(), trigger, action, info, patient, comment, user)) # add)
        database.commit()

    @staticmethod
    def patient_info(user, action, patient):
        """

        Returns string describing what the user does involving the patient's information.

        :param user: user that is accessing/updating info.
        :param action: what the user is doing with the info
        :param patient: the patient's name
        """
        if action == 'view':
            return user + " viewed "+patient+"'s personal information"
        elif action == 'upload':
            return user + " uploaded "+patient+"'s personal information"
        elif action == 'update':
            return user + " updated "+patient+"'s personal information"
        else:
            return 'There is an unrecognized personal information action involving ' \
                   + user + " " + action + " " + patient

    @staticmethod
    def patient_transfer(user, patient, from_hospital, to_hospital):
        """

        Returns a string describes the admission/discharge/transfer of a patient.

        :param: from_hospital: the hospital the patient is coming from
        :param: to_hosital: the hospital the patient is going to
        :param: patient: the patient's name

        Will also handle admission/discharge to/from a hospital. The appropriate parameter will be None.
        """
        if from_hospital == '':
            return patient + ' is admitted to ' + to_hospital+'.'
        elif to_hospital == '':
            return patient + ' is discharged from ' + from_hospital + '.'
        else:
            return patient + ' was transferred from ' + from_hospital + ' to ' + to_hospital + '.'

    @staticmethod
    def prescription(user, action, info, patient):
        """

        Returns a string describing the user's actions involving prescriptions.

        :param user: user triggering the log.
        :param action: add/refill/remove/view
        :param info: information about the action
        :param patient: the patient's name
        """
        if action == 'add':
            return user + ' wrote a prescription of ' + info + ' for ' + patient + '.'
        elif action == 'refill':
            return user + ' refilled a prescription of ' + info + ' for ' + patient + '.'
        elif action == 'remove':
            return user + ' removed a prescription of ' + info + ' for ' + patient + '.'
        elif action == 'view':
            return user + " viewed " + patient + "'s prescriptions." # of " + info + "."
        elif action == 'edit':
            return user + " edited " + patient + "'s prescription of " + info + "."
        else:
            return 'There is an unrecognized prescription action involving ' + user + ', ' + action + ', ' \
                   + info + ', and ' + patient

    @staticmethod
    def appointment(user, action, info, patient):
        """

        Returns a string about a users action involving an appointment.

        :param: user: the user that'll being altering the appointment
        :param: action: add/edit/cancel an appointment.
        :param: patient: the patient who's appointment is being altered.
        """
        if action == 'create':
            return user + ' created an appointment for ' + patient + ' invloving ' + info +'.'
        elif action == 'edit':
            return user + ' edited an appointment for ' + patient + ' with Doctor ' + info +'.'
        elif action == 'cancel':
            return user + ' canceled an appointment for ' + patient + ' with Doctor ' + info +'.'
        else:
            return 'There is an unrecognized appointment action involving ' + user + ', ' + action + \
                   ', and ' + patient + ' with Doctor ' + info +'.'

    @staticmethod
    def test_results(user, action, info, patient):
        """

        Returns a string describing the users actions involving the test results.

        :param user: user triggering the log.
        :param action: upload/release/view
        :param info: information about the test
        :param patient: the patient's name
        """
        if action == 'upload':
            return user + ' uploaded ' + info + ' test results for ' + patient + '.'
        elif action == 'release':
            return user + ' released ' + info + ' test results for ' + patient + '.'
        elif action == 'view':
            return user + ' viewed ' + info + ' test results for ' + patient + '.'
        elif action == 'delete':
            return user + ' deleted ' + info + ' test results for ' + patient + '.'
        else:
            return 'There is an unrecognized test result action involving ' + user + ', ' + action + ', ' \
                   + info + ', and ' + patient


    @staticmethod
    def log_in(user):
        """

        Returns a string describing a user logging in.

        :param user: the user logging in.
        :return: string
        """
        return user + " logged on."

    @staticmethod
    def register(user):
        """

        Returns a string describing a user registering.

        :param user: the user registering
        :return: string
        """
        return user + " registered."

    @staticmethod
    def calendar(user):
        """

        Returns a string describing a user involving the calendar.

        :param user: the user viewing the calendar.
        :return: string
        """
        return user + ' viewed their calendar.'

    @staticmethod
    def auth(user,patient):
        return user + " authorized "  + patient+"."

    @staticmethod
    def message(user,patient):
        return user + " sent a message to " + patient+"."

    @staticmethod
    def ImpExp(user, action):
        if action == 'Imp':
            return user + " imported information to the database."
        elif action == 'Exp':
            return user + " exported their information."
        else:
            return "There was an unrecognized import/export action involving " + user + " and " + action + "."

    @staticmethod
    def unknown(trigger,user,action,info,patient):
        """

        Returns a string describing an unknown action.

        :param trigger: the module that triggers the log.
        :param user: user triggering the log.
        :param action: the action triggering the log
        :param info: information about the action
        :param patient: the patient's name
        :return: string
        """
        return "An unknown event involving " + trigger + ', ' + user + ", " + action + ", " + info + \
               ", and " + patient + " has occurred."

    @staticmethod
    def read_log(): # , lines_to_view):
        """
        Counts all the lines in the log file. Then prints the last X lines in log.txt, specified by the user.
        """
        """
        log_lines = ""
        for line in open('./log.txt'):
            log_lines += line
        return log_lines
        """
        return Log.objects.order_by("time").reverse()

    def __str__(self):
        return str(self.time) + " " + self.comment + "\n"
"""
Stats to be tracked:
# of Patients
Number of visits per patient
Average length of stay
Common admission reasons
prescription stats (Most common, doc prescribing the most, etc)

"""


class Stats:

    @staticmethod
    def num_user():
        """
        Number of all types of users in the system.
        :return:
        """
        db.execute("select username from auth_user")
        users = db.fetchall()
        num_user = len(users)
        return num_user

    @staticmethod
    def num_patients():
        """
        Number of patients in the system.
        :return:
        """
        db.execute("select email from registration_patient")
        users = db.fetchall()
        num_pat = len(users)
        return num_pat

    @staticmethod
    def num_doctors():
        """
        Number of doctors in the system.
        :return:
        """
        db.execute("select email from registration_doctor")
        users = db.fetchall()
        num_doc = len(users)
        return num_doc

    @staticmethod
    def num_admin():
        """
        :return: Number of administrators in the system.
        """
        db.execute("select email from registration_admin")
        users = db.fetchall()
        num_admin = len(users)
        return num_admin

    @staticmethod
    def num_nurse():
        db.execute("select email from registration_nurse")
        users = db.fetchall()
        num_nurse = len(users)
        return num_nurse

    @staticmethod
    def num_admit():
        """
        Returns the number of patients in the hospitals.
        """
        db.execute("select name from Admission_Discharge_admission_discharge")
        patients = db.fetchall()
        admit = len(patients)

        return admit

    @staticmethod
    def num_visits():
        """
        Returns the average number of appointments per patient.
        """
        visits=[]
        #db.execute("select patient from appointments_appointment")
        #visits = db.fetchall()
        visits_num = len(visits)
        patients = []
        for item in visits:
            if item[0] in patients:
                patients+=item[0]
        patient_num = len(patients)
        if patient_num == 0:
            return 0
        return visits_num/patient_num

    @staticmethod
    def visit_length():
        """
        Average visit length.
        """
        db.execute("select start_time,end_time from appointments_appointment")
        visits = db.fetchall()
        tm=datetime.timedelta(0,0,0)
        for item in visits:
            tm+=item[0]-time[1]
        visit_num = len(visits)
        if visit_num == 0:
            return 0
        return sec_to_time(tm.seconds/visit_num)

    @staticmethod
    def sec_to_time(time):
        """
        :param time: the number of seconds.
        :return: string represting dd:hh:mm:ss
        """
        sec = time

        days = sec / 86400
        sec -= 86400*days

        hrs = sec / 3600
        sec -= 3600*hrs

        mins = sec / 60
        sec -= 60*mins
        return (days, ':', hrs, ':', min, ':', sec)

    @staticmethod
    def admission_reason():
        """
        Finds the X most common reason(s) for admission to the hospital.
        """
        reason1 = "Common Cold"
        reason2 = "Influenza"
        reason3 = "Colitis"
        reasons = reason1 + ", " + reason2 + ", " +reason3

        return reasons

    @staticmethod
    def prescription_stats():
        """
        Display stats about common prescriptions and their prescribers.
        """
        allprescrips = ""
        presc = []
        db.execute("select medication from prescriptions_prescription")
        presc = db.fetchall()

        for item in presc:
            allprescrips += item[0] + ","
        allprescrips = allprescrips[0:len(allprescrips)-1]
        common = allprescrips.split(",")
        most_common_dict = {}
        for item in common:
            if most_common_dict.__contains__(item):
                most_common_dict[item] += 1
            elif not(most_common_dict.__contains__(item)) and ((item is not None) or (item is not '')):
                most_common_dict[item] = 1
        most_common_string = ""
        for item in most_common_dict:
            most_common_string += str(item) + ":" + str(most_common_dict[item]) + "!"
        sorting = most_common_string.split("!")
        allprescrips = ""
        sorting.sort()
        #sorting.reverse()
        for item in sorting:
            if item is not "":
                allprescrips += item + ", "

        return allprescrips