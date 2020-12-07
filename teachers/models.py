from django.db import models
from datetime import date
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
from PIL import Image

User = get_user_model()

GENDER = (
    ('','Please select'),
    ('male','Male'),
    ('Female','Female')
)

JOB_TYPE = (
    ('','Please select'),
    ('permanent','Permanent'),
    ('temporary','Temporary'),
    ('contract_work','Contract Work'),
    ('guest','Guest')
)

EMPYOYEE_TYPE = (
    ('','Please select'),
    ('teaching_staff','Teaching Staff'),
    ('non_teaching_staff','Non Teaching Staff')
)


ATTENDANCE_TYPE= (
    ('','Please select'),
    ('all','All'),
    ('designations','Designations')
)

ATTENDANCE_HOURS_TYPE= (
    ('','Please select'),
    ('am','AM'),
    ('pm','PM'),
    ('full_day','Full_Day')
)


LEAVE_CATEGORY= (
    ('','Please select'),
    ('first_half','First_Half'),
    ('second_half','Second_Half')
)

ACTION_TAKEN = (
    ('', 'please select'),
    ('parental_involvement', 'Parental Involvement'),
    ('guadance_and_counselling', 'Guadance And Counselling'),
    ('suspension', 'Suspension'),
    ('dismissal', 'Dismissal'),
    ('others', 'Others')

)


class Teacher(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)   

    employee_name = models.CharField(max_length=200, verbose_name='Employee Name')
    address = models.CharField(max_length=50, verbose_name='Address')
    postal_code = models.CharField(max_length=50, verbose_name='Postal Code')
    country = CountryField(default= 'TZ', verbose_name='Country')
    nationality = CountryField(default= 'TZ', verbose_name='Nationality')
    gender = models.CharField(max_length=10, verbose_name='Gender', choices=GENDER)
    joining_date = models.DateTimeField(verbose_name='Date', default = True)
    mobile_number = models.CharField(max_length=20, verbose_name='Mobile Number')
    phone_number = models.CharField(max_length=20, verbose_name='Phone Number')
    date_of_birth = models.DateField(verbose_name='Birth Date', blank=True, null=True)
    email = models.EmailField(verbose_name='Email Address')
    job_type = models.CharField(max_length=50, verbose_name='Job Type', choices=JOB_TYPE)
    emp_type = models.CharField(max_length=50, verbose_name='Employee Type', choices=EMPYOYEE_TYPE)
    designations = models.CharField(max_length=50, verbose_name='Designations')
    termination_date = models.DateField(verbose_name='Termination Date')

    def __str__(self):
        return self.mobile_number 


class TeacherAttendance(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 

    date = models.DateTimeField(verbose_name='Date', default = True)
    type = models.CharField(max_length=50, verbose_name='Attendance Type', choices=ATTENDANCE_TYPE)
    name = models.CharField(max_length=200, verbose_name='Name')
    attendance_hours = models.CharField(max_length=10, verbose_name='Attendance Hours Type', choices=ATTENDANCE_HOURS_TYPE)
    description = models.TextField()
    leave_category = models.CharField(max_length=50, verbose_name='Leave Category', choices=LEAVE_CATEGORY)

    def __str__(self):
        return self.name 


class StaffDescipline(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    staff_name = models.CharField(max_length=200, verbose_name='Staff Name')
    designation = models.CharField(max_length=200, verbose_name='Designation')
    description = models.TextField()
    description_date = models.DateField(verbose_name='Descripton Date')
    action_taken = models.CharField(max_length=50, verbose_name='Action Taken', choices=ACTION_TAKEN)
    from_date = models.DateField(verbose_name='From Date')
    to_date = models.DateField(verbose_name='To Date')
    fine_amount = models.DecimalField(max_digits=6, decimal_places=0)
    staff_in_charge = models.CharField(max_length=50, verbose_name='Staff In Charge')
    paid_fine_amount = models.BooleanField()


    def __str__(self):
        return self.staff_name