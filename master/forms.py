from django import forms

from .models import School

class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        exclude = ('master',)
        widgets = {
          'address': forms.Textarea(attrs={'rows':3, 'cols':15}),
        }