from django import forms

from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory

from .models import Class, Stream, Subject, ClassSyllabus


class StreamForm(forms.ModelForm):

    class Meta:
        model = Stream
        fields = ('name',)

class ClassForm(forms.ModelForm):

    class Meta:
        model = Class
        fields = ('name', 'stream', 'seat','class_teacher', 'leaders',)


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ('name', 'short_name', 'department',)


class ClassSyllabusForm(forms.ModelForm):

    class Meta:
        model = ClassSyllabus
        fields = ('id','subjects', 'select_class', 'theory', 'assignment', 'practical', 'project',)


ClassSyllabusFormSet = formset_factory(ClassSyllabusForm, extra=0)

ClassSyllabusInlineFormSet = inlineformset_factory(Class, ClassSyllabus, fields = ('id','subjects', 'theory', 'assignment', 'practical', 'project',), extra=1)