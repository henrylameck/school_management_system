from django import forms

from .models import School, Department, Semester, AcademicSession, AcademicYear

class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        exclude = ('master',)
        widgets = {
          'address': forms.Textarea(attrs={'rows':3, 'cols':15}),
        }


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        exclude = ['created_by', ]


class SemesterForm(forms.ModelForm):

    class Meta:
        model = Semester
        exclude = ['created_by', ]


class AcademicSessionForm(forms.ModelForm):
  
    class Meta:
        model = AcademicSession
        exclude = ['created_by','is_closed', ]

class UpdateAcademicSessionForm(forms.ModelForm):
  
    class Meta:
        model = AcademicSession
        exclude = ['created_by', ]

class AcademicYearForm(forms.ModelForm):
  
    class Meta:
        model = AcademicYear
        exclude = '__all__'