from django import forms

from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory

from .models import *


class ExamMasterForm(forms.ModelForm):

    class Meta:
        model = ExamMaster
        fields = ('name', 'select_class', 'enter_code', 'select_term',)


ExamSubjectInlineFormSet = inlineformset_factory(ExamMaster, ExamSubject, fields = ('id','subject', 'assignment_marks_min', 'assignment_marks_max', 'theory_marks_min', 'theory_marks_max','practical_marks_min', 'practical_marks_max', 'project_marks_min', 'project_marks_max', 'total_marks_max',), extra=1)