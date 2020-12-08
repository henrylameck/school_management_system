from django.db import models
from django.contrib.auth import get_user_model

from classes.models import Class, Subject, SubjectPart
from students.models import StudentAdmission

User = get_user_model()


SELECT_TERM = (
    ('', 'please select'),
    ('term_one', 'Term 1'),
    ('term_two', 'Term 2'), 
)

class ExamMaster(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    name = models.CharField(max_length=50, verbose_name='Exam Name')
    select_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    enter_code = models.CharField(max_length=50, verbose_name='Enter Examination Code')
    select_term = models.CharField(max_length=50, verbose_name='Select Term', choices=SELECT_TERM)

    def __str__(self):
        return str(self.id)


class ExamSubject(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    exam_master = models.ForeignKey(ExamMaster, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assignment_marks_min = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Assignment Marks Min', default=0.00)
    assignment_marks_max = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Assignment Marks Max', default=100.00)
    theory_marks_min = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Theory Marks min', default=0.00)
    theory_marks_max = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Theory Marks max', default=100.00)
    practical_marks_min = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Practical Marks min', default=0.00)
    practical_marks_max = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Practical Marks max', default=100.00)
    project_marks_min = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Project Marks min', default=0.00)
    project_marks_max = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Project Marks max', default=100.00)
    total_marks_max = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='Total Marks max', default=100.00)

    def __str__(self):
        return self.subject.name


class ExamDivision(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    name = models.CharField(max_length=20, verbose_name='Division Name')
    percentage_from = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Percentage From')
    percentage_to = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Percentage To')

    def __str__(self):
        return str(self.name)


COMPONENT_TYPE = (
    ('', 'please select'),
    ('theory', 'Theory'),
    ('practical', 'Practical'),
    ('assignment', 'Assignment'),
    ('project', 'Project'),
)

class ExamGrade(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    name = models.CharField(max_length=20, verbose_name='Enter Grade Name')
    percentage_from = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Percentage From')
    percentage_to = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Percentage To')
    component = models.CharField(max_length=20, verbose_name='Component Type', choices=COMPONENT_TYPE)
    status = models.BooleanField(verbose_name='Fail Grade', default=False)

    def __str__(self):
        return self.name


class ExamMarkMaster(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    exam_division = models.ForeignKey(ExamDivision, on_delete=models.CASCADE)
    exam_subject = models.ForeignKey(ExamSubject, on_delete=models.CASCADE)


SUBJECT_PART = (
    ('', 'please select'),
    ('paper_one', 'Paper 1'),
    ('paper_two', 'Paper 2'),
)

class ExamMarkEntry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    exam_mark_master = models.ForeignKey(ExamMarkMaster, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentAdmission, on_delete=models.CASCADE)
    theory_mark = models.CharField(max_length=18, verbose_name='Theory Marks')
    assignment_mark = models.CharField(max_length=18, verbose_name='Assignment Marks')
    practical_mark = models.CharField(max_length=18, verbose_name='Practical Marks')
    project_mark = models.CharField(max_length=18, verbose_name='Project Marks')
    subject_part = models.ForeignKey(SubjectPart, verbose_name='Subject Part', on_delete=models.CASCADE)
    total = models.CharField(max_length=50, verbose_name='Total', blank=True, null=True)

    def __str__(self):
        return self.student


    def save(self, *args, **kwargs): 
        self.total = self.theory_mark + self.assignment_mark + self.project_mark + self.practical_mark
        super(ExamMarkEntry, self).save(*args, **kwargs) 


class ExamMarkEntryPart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    exam_mark_master = models.ForeignKey(ExamMarkMaster, on_delete=models.CASCADE)
    subject_part = models.ForeignKey(SubjectPart, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentAdmission, on_delete=models.CASCADE)
    theory_mark = models.CharField(max_length=18, verbose_name='Theory Marks')
    assignment_mark = models.CharField(max_length=18, verbose_name='Assignment Marks')
    practical_mark = models.CharField(max_length=18, verbose_name='Practical Marks')
    project_mark = models.CharField(max_length=18, verbose_name='Project Marks')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.student

