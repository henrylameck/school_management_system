from django.db import models
from datetime import date
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

from PIL import Image

User = get_user_model()

GENDER = (
    ('','Please select'),
    ('male','Male'),
    ('Female','Female')
)

PHONE_STATUS = (
    ('','Please select'),
    ('received','Received'),
    ('dialed','Dialed')
)


class ApplicationFormSale(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    date = models.DateTimeField(verbose_name='Date', default=date.today) 
    form_number = models.CharField(max_length=20, verbose_name='Form Number', unique=True)
    serial_number = models.CharField(max_length=20, verbose_name='Serial Number', unique=True)
    amount = models.FloatField(verbose_name='Amount')
    first_name = models.CharField(max_length=200, verbose_name='First Name')
    middle_name = models.CharField(max_length=200, verbose_name='Middle Name')
    last_name = models.CharField(max_length=200, verbose_name='Last Name')
    phone_number = PhoneNumberField(verbose_name='Phone Number')

    def __self__(self):
        return self.form_number

class ApplicationFormReceive(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    date = models.DateTimeField(verbose_name='Date', default=date.today) 
    application_number = models.CharField(max_length=20, verbose_name='Application Number')
    serial_number = models.CharField(max_length=20, verbose_name='Serial Number')
    Student_name = models.CharField(max_length=200, verbose_name='First Name')
    gender = models.CharField(max_length=10, verbose_name='Gender', choices=GENDER)
    date_of_birth = models.DateField(verbose_name='Birth Date', blank=True, null=True)
    gurdian_name = models.CharField(max_length=200, verbose_name='Gurdian Name')
    phone_number = PhoneNumberField(verbose_name='Phone Number')

    def __self__(self):
        return self.form_number

    
class VisitorsEnquiry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    enquiry_date = models.DateTimeField(verbose_name='Enquiry Date', default = True) 
    visitor_name = models.CharField(max_length=200, verbose_name='Visitor Name')
    address = models.CharField(max_length=50, verbose_name='Address')
    phone_number = PhoneNumberField(verbose_name='Phone Number')
    description = models.TextField()
    Student_name = models.CharField(max_length=200, verbose_name='Student Name')
    admission_number = models.CharField(max_length=200, verbose_name='Admission Number')
    staff_name = models.CharField(max_length=200, verbose_name='Staff Name')
    designations = models.CharField(max_length=50, verbose_name='Designations')

    def __self__(self):
        return self.phone_number


class PhoneRegister(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    date = models.DateTimeField(verbose_name='Date', default = True) 
    phone_status = models.CharField(max_length=10, verbose_name='Phone_status', choices=PHONE_STATUS)
    phone_number = PhoneNumberField(verbose_name='Phone Number')
    reference_person_name = models.CharField(max_length=50, verbose_name='Reference Person Name')
    reference_person_remarks = models.TextField()

    def __self__(self):
        return self.phone_number