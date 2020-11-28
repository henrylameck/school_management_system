from django import forms

from .models import Class, Stream, Subject, ClassSyllabus


class StreamForm(forms.ModelForm):

    class Meta:
        model = Stream
        fields = ('name',)

class ClassForm(forms.ModelForm):

    class Meta:
        model = Class
        fields = ('name', 'stream', 'seat',)


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ('name', 'short_name', 'department',)


class ClassSyllabusForm(forms.ModelForm):

    class Meta:
        model = ClassSyllabus
        fields = ('select_class', 'subjects', 'components', )