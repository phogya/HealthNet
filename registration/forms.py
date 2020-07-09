from django import forms
from django.contrib.auth.models import User
from .models import *
__author__ = 'Melissa'
from django.contrib.auth.forms import UserCreationForm

SMOKER_OPTIONS = [
    ('never', 'Never'),
    ('sometimes', 'Sometime'),
    ('often', 'Often'),
    ('daily', 'Daily'),
]

PAST_ILLS =[
    ('high blood pressure', 'High Blood Pressure'),
    ('low blood pressure', 'Low Blood Pressure'),
    ('diabetes', 'Diabetes'),
    ('heart disease', 'Heart Disease'),
    ('hemophilia', 'Hemophilia'),
    ('arthritis', 'Arthritis'),
    ('epilepsy', 'Epilepsy'),
    ('cancer', 'Cancer'),
    ('None', 'None'),
]

MARRIAGE_STAT = [
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Divorced', 'Divorced'),
    ('Widow', 'Widow'),
]


SEX = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),

]


class PatientForm(forms.ModelForm):
    """
    Creates a patient form based off the user creation form
    """
    email = forms.EmailField(required=True)

    class Meta:
        model=Patient
        password = forms.CharField(widget=forms.PasswordInput)
        widgets ={
            'password':forms.PasswordInput(),
        }
        fields = ["first_name", "last_name","email", "password", "phone_number"]


class Med_Info_Form(forms.ModelForm):

    is_smoker = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices =SMOKER_OPTIONS)
    is_drinker = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices =SMOKER_OPTIONS)
    past_illnesses =  forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple, choices =PAST_ILLS)
    class Meta:
        model = Med_Info
        fields = ["is_smoker","is_drinker","allergies","past_illnesses"]
'''

which doctors do they work
'''




class NurseForm(forms.ModelForm):

    email = forms.EmailField(required=True)
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = Nurse
        widgets ={
            'password':forms.PasswordInput(),
        }
        fields = ["first_name", "last_name","email", "password", "phone_number"]

class Main_User(User):
    """
    The basis attributes for all the user types
    """

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()
    phone_num = forms.IntegerField()



class DoctorForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Doctor
        password = forms.CharField(widget=forms.PasswordInput)
        widgets ={
            'password':forms.PasswordInput(),
        }
        fields = ["first_name", "last_name","email", "password","phone_number"]

class AdminForm(forms.ModelForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = Admin
        password = forms.CharField(widget=forms.PasswordInput)
        widgets ={
            'password':forms.PasswordInput(),
        }
        fields = ["first_name", "last_name", "email", "password","phone_number"]

class Personal_Info_Form(forms.ModelForm):

    marital_status = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=MARRIAGE_STAT)
    sex = forms.ChoiceField(required=True,widget=forms.RadioSelect, choices=SEX)
    class Meta:
        model=Personal_Info
        fields =["insurance_Number", "insurance_Name", "name_Of_Emergency_Contact" , "number_Of_Emergency_Contact", "sex", "weight_lbs","height_inches", "marital_status"]
