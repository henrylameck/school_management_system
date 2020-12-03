from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model

from classes.models import Class, Stream


User = get_user_model()

GENDER = (
    ('','Please select'),
    ('male','Male'),
    ('Female','Female')
)

RELIGION = (
    ('','Please select'),
    ('christianity', 'Christianity'),
    ('islamic', 'Islamic'),
    ('hinduism', 'Hinduism'),
    ('Buddhism', 'Buddhism'),
    ('Others', 'Others')
)

BLOOD_GROUP = (
    ('','Please select'),
    ('a+', 'A+'),
    ('o+', 'O+'),
    ('b+', 'B+'),
    ('ab+', 'AB+'),
    ('a-', 'A-'),
    ('o-', 'O-'),
    ('b-', 'B-'),
    ('ab-', 'AB-')
)

FATHER_OCCUPATION = (
    ('','Please select'),
    ('Agriculture', 'Agriculture'),
    ('Banker', 'Banker'),
    ('Business', 'Business'),
    ('Doctor', 'Doctor'),
    ('Farmer', 'Farmer'),
    ('Fisherman', 'Fisherman'),
    ('Public Service', 'Public Service'),
    ('Private Service', 'Private Service'),
    ('Shopkeeper', 'Shopkeeper'),
    ('Driver', 'Driver'),
    ('Worker', 'Worker'),
    ('N/A', 'N/A'),
)

MOTHER_OCCUPATION = (
    ('','Please select'),
    ('Agriculture', 'Agriculture'),
    ('Banker', 'Banker'),
    ('Business', 'Business'),
    ('Doctor', 'Doctor'),
    ('Farmer', 'Farmer'),
    ('Fisherman', 'Fisherman'),
    ('Public Service', 'Public Service'),
    ('Private Service', 'Private Service'),
    ('Shopkeeper', 'Shopkeeper'),
    ('Driver', 'Driver'),
    ('Worker', 'Worker'),
    ('N/A', 'N/A'),
)

GURDIAN_OCCUPATION = (
    ('','Please select'),
    ('Agriculture', 'Agriculture'),
    ('Banker', 'Banker'),
    ('Business', 'Business'),
    ('Doctor', 'Doctor'),
    ('Farmer', 'Farmer'),
    ('Fisherman', 'Fisherman'),
    ('Public Service', 'Public Service'),
    ('Private Service', 'Private Service'),
    ('Shopkeeper', 'Shopkeeper'),
    ('Driver', 'Driver'),
    ('Worker', 'Worker'),
    ('N/A', 'N/A'),
)

STUDENT_TYPE = (
    ('','Please select'),
    ('day', 'Day'),
    ('boarding', 'Boarding'),
    ('school bus', 'School Bus')
)

ATTENDANCES_TYPE = (
    ('', 'Please select'),
    ('present', 'Present'),
    ('absent', 'Absent')

)


class PersonalDetails(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    first_name = models.CharField(max_length=200, verbose_name='First Name')
    middle_name = models.CharField(max_length=200, verbose_name='Middle Name')
    last_name = models.CharField(max_length=200, verbose_name='Last Name')
    initial_expansion = models.CharField(max_length=200, verbose_name='Initial Expansion')
    date_of_birth = models.DateField(verbose_name='Date Of Birth')
    gender = models.CharField(max_length=10, verbose_name='Gender', choices=GENDER)
    place_of_birth = models.CharField(max_length=200, verbose_name='Place of Birth')
    father_name = models.CharField(max_length=200, verbose_name='Father Name')
    father_occupation = models.CharField(max_length=200, verbose_name='Father Occupation', choices=FATHER_OCCUPATION)
    mother_name = models.CharField(max_length=200, verbose_name='Mother Name')
    mother_occupation = models.CharField(max_length=200, verbose_name='Mother Occupation', choices=MOTHER_OCCUPATION)
    gurdian_name = models.CharField(max_length=200, verbose_name='Gurdian Name')
    gurdian_occupation = models.CharField(max_length=200, verbose_name='Gurdian Occupation', choices=GURDIAN_OCCUPATION)
    Notes = models.TextField(verbose_name='Notes')
    relationship = models.CharField(max_length=200, verbose_name='Relationship')
    nationality =CountryField(default= 'TZ', verbose_name='Nationality')
    religion = models.CharField(max_length=20, verbose_name='Religion', choices=RELIGION)
    blood_group = models.CharField(max_length=10, verbose_name='Blood Group', choices=BLOOD_GROUP)
    student_type =models.CharField(max_length=20, verbose_name='Student Type', choices=STUDENT_TYPE)
    passport = models.ImageField(upload_to='passport', verbose_name='Upload Passport')


    def __str__(self):
        return self.first_name + '' + self.last_name


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


class HostelAllocation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    gender = models.CharField(max_length=20, choices=GENDER)
    date = models.DateField(verbose_name='Allocation Date')
    hostel_name = models.CharField(max_length=200, verbose_name='Hostel Name')
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


class StudentRegistration(models.Model):
    personal_details = models.ForeignKey(PersonalDetails,on_delete=models.PROTECT)
    student_admission = models.ForeignKey(StudentAdmission,on_delete=models.PROTECT)
    personal_contact_detail= models.ForeignKey(PersonalContactDetail,on_delete=models.PROTECT)
    transport_allocation= models.ForeignKey(TransportAllocation,on_delete=models.PROTECT)
    hostel_allocation= models.ForeignKey(HostelAllocation,on_delete=models.PROTECT)
    qualification= models.ForeignKey(Qualification,on_delete=models.PROTECT)
    feecollection= models.ForeignKey(FeeCollection,on_delete=models.PROTECT)

class EnrolledStudent(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    
    class_name = models.ForeignKey(Class, on_delete=models.DO_NOTHING, null=True)
    stream = models.ForeignKey(Stream, on_delete=models.DO_NOTHING, null=True)
    student = models.ForeignKey(StudentRegistration,on_delete=models.PROTECT)
    roll = models.IntegerField()

    def __str__(self):
        return self.student


class Attendances(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

	student = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE, related_name='student_attendance')
	type = models.IntegerField(choices=ATTENDANCES_TYPE, default=0)
	motif = models.TextField(null=True, blank=True) # REM.: should have been "reason"; redundant with "justification" fiel
	is_excused = models.BooleanField(default=False)
	justification = models.TextField(null=True, blank=True)
	document = models.FileField(related_name='document_attendance', null=True, blank=True)
	start_date = models.DateField(null=True, default=date.today)
	finish_date = models.DateField(null=True, blank=True)
	comment = models.CharField(max_length=255, null=True, blank=True) # Free text
    
	
	def __str__(self):
		return '{0} - {1}'.format(self.student, self.type)
		
	class Meta:
		ordering = ('-start_date','-modified_at',)
		verbose_name = _("Attendance")
		verbose_name_plural = _("Attendances")


class Discipline_type(models.Model):	
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

	punishment = models.CharField(max_length=100, null=True)
	start_date = models.BooleanField(default=True)
	end_date = models.BooleanField(default=True)
	start_time = models.BooleanField(default=True)
	end_time = models.BooleanField(default=False)
	repeatable = models.BooleanField(default=True)
	alert = models.PositiveSmallIntegerField(default=0)
	description = models.CharField(max_length=255, null=True, blank=True)
	comment = models.CharField(max_length=255, null=True, blank=True) # Free text
	
	def __str__(self):
		return '{0}'.format(self.punishment)
	
	class Meta:
		ordering = ('punishment',)
		verbose_name = _("Discipline's type")
		verbose_name_plural = _("Discipline's types")


STATUS = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('done', 'Done'),
    ('cancelled', 'cancelled')

)


class Disciplines(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

	type = models.ForeignKey(to='Discipline_type', on_delete=models.SET_NULL, related_name='discipline_type', null=True, blank=True, default=1)
	student = models.ForeignKey(StudentRegistration, on_delete=models.CASCADE, related_name='student_discipline')
	motif = TextField(null=True, blank=True)
	fact_date = models.DateField(null=True, blank=True, default=date.today)
	status = models.IntegerField(choices=STATUS, default=ACTIVE, null=True, blank=True)
	location = models.CharField(max_length=100, null=True, blank=True) 
	comment = models.CharField(max_length=255, null=True, blank=True) # Free text

	
	def __str__(self):
		return '{0}'.format(self.type)
	
	class Meta:
		ordering = ('-fact_date',)
		verbose_name = _('Discipline')
		verbose_name_plural = _('Disciplines')	


class Disciplines_Details(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

	discipline = models.ForeignKey(to='Disciplines', on_delete=models.CASCADE, related_name='discipline_detail')
	start_date = models.DateField(null=True, blank=True)
	start_time = models.TimeField(null=True, blank=True)
	finish_date = models.DateField(null=True, blank=True)
	finish_time = models.TimeField(null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	
	
	def __str__(self):
		return '{0}'.format(self.id)
		
	class Meta:
		verbose_name = _('Discipline details')
		verbose_name_plural = _('Disciplines details')
		
