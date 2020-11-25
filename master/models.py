from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model


User = get_user_model()

class School(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    master = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=250, verbose_name='Name of school')
    code = models.CharField(max_length=100, verbose_name='School Code')
    address = models.TextField()
    postal_code = models.CharField(max_length=100, verbose_name='Postal Code')
    country = CountryField(blank_label='(select country)')
    phone_no_1 = models.CharField(max_length=14)
    phone_no_2 = models.CharField(max_length=14, blank=True)
    fax = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField()
    district = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    starting_date = models.DateField(auto_now_add=True)
    logo = models.ImageField(upload_to='logo', verbose_name='Upload school logo')

    def __str__(self):
        return self.name


class Department(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255, unique=True)

    short_name = models.CharField('Department Short Form', 
        max_length=10)
    code = models.PositiveIntegerField()
    # head = models.ForeignKey(
    #     Teacher, on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def dept_code(self):
        if not self.code:
            return ""
        return self.code

    def __str__(self):
        return str(self.name)



class AcademicSession(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    year = models.PositiveIntegerField(unique=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return '{} - {}'.format(self.year, self.year + 1)


class Semester(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    number = models.PositiveIntegerField(unique=True)
    # guide = models.ForeignKey(
    #     Teacher, on_delete=models.CASCADE, default=None, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        ordering = ['number', ]

    def __str__(self):
        if self.number == 1:
            return '1st Semister'
        if self.number == 2:
            return '2nd Semister'
        if self.number == 3:
            return '3rd Semister'
        if 3 < self.number <= 12:
            return '%sth semister' % self.number

