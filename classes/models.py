from django.db import models
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField

from master.models import Department, Semester

User = get_user_model()


class Stream(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=45, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name


class Class(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20)
    # class_teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True)
    leaders = models.ManyToManyField("students.StudentRegistration")
    seat = models.PositiveIntegerField(verbose_name='No of seats')
    stream = models.ForeignKey(Stream, on_delete=models.SET_NULL, null=True)

    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return "{} {}".format(self.name, self.stream)


class Subject(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.short_name)


COMPONENTS =(
    ('theory', 'Theory'),
    ('practical', 'Practical'),
    ('assignment', 'Assignment'),
    ('project', 'Project'),
)

class ClassSyllabus(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    select_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)
    components = MultiSelectField(choices=COMPONENTS)

    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True, verbose_name='H.O.D')
    
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return '{} {}'.format(self.select_class, self.subjects)
