from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model

from classes.models import Class, Stream


User = get_user_model()


class StudentAdmission(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    reg_no = models.CharField(max_length=100, verbose_name='Admission No:', blank=True, null=True)
    date = models.DateField(verbose_name='Admission date')
    application_form_no = models.CharField(max_length=100, verbose_name='Application Form No:')
    class_name = models.ForeignKey(Class, on_delete=models.DO_NOTHING, null=True)
    stream = models.ForeignKey(Stream, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.reg_no


class PersonalContactDetail(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    #Permanent Address
    p_address = models.TextField(verbose_name="Address")
    p_postal_code = models.CharField(max_length=50, verbose_name='Postal Code')
    p_country = CountryField(default='TZ', verbose_name='Country')
    p_phone = models.CharField(max_length=14, verbose_name='Phone')
    student_email = models.EmailField(verbose_name='Student Email')

    #Present Address
    pr_address = models.TextField(verbose_name="Address")
    pr_postal_code = models.CharField(max_length=50, verbose_name='Postal Code')
    pr_country = CountryField(default='TZ', verbose_name='Country')
    pr_phone = models.CharField(max_length=14, verbose_name='Phone')
    parent_email = models.EmailField(verbose_name='Parent Address')

    def __str__(self):
        return self.parent_email
    

class TransportAllocation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    date = models.DateField(verbose_name='Allocation Date')
    vehicle = models.CharField(max_length=200, verbose_name='Vehicle name')
    route = models.CharField(max_length=200, verbose_name='Route')
    boarding_point = models.CharField(max_length=200, verbose_name='Boarding Point Name')

    def __str__(self):
        return self.vehicle


class Hostelallocation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    gender = models.CharField(max_length=20, choices=GENDER)
    date = models.DateField(verbose_name='Allocation Date')
    hostel_name = models.CharField(max_lenght=200, verbose_name='Hostel Name')
    block_name = models.CharField(max_length=200, verbose_name='Block Name')
    room_name = models.CharField(max_length=200, verbose_name='Room Name')

    def __str__(self):
        return self.hostel_name


class Qualification(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    school_name = models.CharField(max_length=100, verbose_name='School Name')
    date_admission = models.DateField(verbose_name='Admission Date')
    date_leaving = models.DateField(verbose_name='Leaving Date')
    last_exam = models.CharField(max_length=200, verbose_name='Last Attending Examination')
    other_qualification = models.CharField(max_length=200, verbose_name='Other Qualification')
    remarks = models.TextField()

    def __str__(self):
        return self.school_name


PAYMENT_MODE = (
    ('', 'Please select'),
    ('cash', 'Cash'),
    ('cheque', 'Cheque'),
    ('draft', 'Draft'),
)

class FeeCollection(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    payment_mode = models.CharField(max_length=50, verbose_name='Payment Mode', choices=PAYMENT_MODE)
    bank = models.CharField(max_length=200)
    cheque = models.CharField(max_length=200)
    receipt = models.CharField(max_length=200)
    reg_fee_amount = models.CharField(max_length=200)

    def __str__(self):
        return self.payment_mode