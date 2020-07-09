from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import User
from django.contrib.auth.models import Group, AbstractUser
# Create your models here.

class Personal_Info(models.Model):
    """
        I'm storing the users information with a one-to-one relationship
            -name
            -password
            -insurance #
            -email
            -patient id?
    """
    insurance_Number = models.CharField(max_length=10) #check for double insurance
    insurance_Name = models.CharField(max_length=20)
    name_Of_Emergency_Contact = models.CharField(max_length=100)
    number_Of_Emergency_Contact = models.CharField(max_length=100)
    sex = models.CharField(max_length=20)
    weight_lbs = models.IntegerField()
    height_inches = models.IntegerField()
    marital_status = models.CharField(max_length=20)



class Med_Info(models.Model):
    """
    A separate place for just a patients past medical info
    """
    is_smoker = models.CharField(max_length=20)
    is_drinker = models.CharField(max_length=20)
    allergies = models.TextField(default="None")
    past_illnesses = models.CharField(max_length=200)



class GenericUser():


    #for R2 everyone will have a DOB in user
    phone_Num = models.CharField(max_length=10)

    email = models.CharField(max_length=100)


class Nurse(models.Model):


    '''
    class Meta:
        permissions=(


        )
    '''
    nurse_id = models.CharField(max_length=10, default="default")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    #confirmPassword = models.CharField(max_length=200)


class Patient(models.Model):
    '''
    class Meta:

        permission = (


        )
    '''

    patient_id = models.CharField(max_length=10, default="default")
    hospital = models.CharField(max_length=100, default="default")
    doctor_id = models.CharField(max_length=10, default="default")

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    #confirmPassword = models.CharField(max_length=30)
    med_info = Med_Info()
    personal_info = Personal_Info()
      # REQUIRED_FIELDS = ['first_name','last_name','email','insurance_num',
    #                   'insurance_name', 'ICE_name', 'ICE_num', 'medications']


class Doctor(models.Model):

    '''
    class Meta:
        permissions = (


        )
    '''
    doctor_id = models.CharField(max_length=10, default="default")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    #confirmPassword = models.CharField(max_length=200)

class Admin(models.Model):
    '''
    class Meta:
        permissions = (


        )
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    #confirmPassword = models.CharField(max_length=200)
