from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model

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