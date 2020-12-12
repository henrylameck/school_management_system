from django import forms
from datetime import date

from django.forms.formsets import formset_factory
from tinymce.widgets import TinyMCE

from .models import *


class PersonalDetailsForm(forms.ModelForm):

    date_of_birth = forms.DateField(
    widget=forms.TextInput(     
        attrs={'type': 'date'} 
        )
    ) 

    class Meta:
        model = PersonalDetails
        exclude = ['created_by',]
        widgets = {
          'notes': forms.Textarea(attrs={'rows':3, 'cols':15}),
        }


class StudentAdmissionForm(forms.ModelForm):
    date = forms.DateField(label='Admission Date', initial=date.today,
    widget=forms.TextInput(     
        attrs={'type': 'date'} 
        )
    )

    class Meta:
        model = StudentAdmission
        exclude = ['created_by',]

    def __init__(self, *args, **kwargs):
        super(StudentAdmissionForm, self).__init__(*args, **kwargs)
        self.fields['roll'].disabled = True



class PersonalContactDetailForm(forms.ModelForm):

    class Meta:
        model = PersonalContactDetail
        exclude = ['created_by',]
        widgets = {
          'p_address': forms.Textarea(attrs={'rows':3, 'cols':15}),
          'pr_address': forms.Textarea(attrs={'rows':3, 'cols':15}),
        }


class TransportAllocationForm(forms.ModelForm):

    date = forms.DateField(label='Allocation Date', initial=date.today, required=False,
    widget=forms.TextInput(     
        attrs={'type': 'date'} 
        )
    ) 

    class Meta:
        model = TransportAllocation
        exclude = ['created_by',]


class HostelAllocationForm(forms.ModelForm):

    date = forms.DateField(label='Allocation Date', initial=date.today, required=False,
        widget=forms.TextInput(     
        attrs={'type': 'date'} 
        )
    ) 

    class Meta:
        model = HostelAllocation
        exclude = ['created_by',]


class QualificationForm(forms.ModelForm):
    date_admission = forms.DateField(label='Date Admission', initial=date.today,
    widget=forms.TextInput(     
        attrs={'type': 'date'} 
        )
    ) 
    date_leaving = forms.DateField(label='Date Leaving', initial=date.today,
    widget=forms.TextInput(     
        attrs={'type': 'date'} 
        )
    )

    class Meta:
        model = Qualification
        exclude = ['created_by',]



class FeeCollectionForm(forms.ModelForm):

    class Meta:
        model = FeeCollection
        fields = ['payment_mode', 'bank', 'cheque', 'reg_fee_amount', 'vehicle_fee_amount', 'receipt',]

    def clean_bank(self):
        payment_mode = self.cleaned_data['payment_mode']
        bank = self.cleaned_data['bank']
        
        if payment_mode == 'draft' or payment_mode == 'cheque':
            if not bank:
                raise forms.ValidationError('The field is Required')
            return bank

    def clean_cheque(self):
        payment_mode = self.cleaned_data['payment_mode']
        cheque = self.cleaned_data['cheque']
        
        if payment_mode == 'draft' or payment_mode == 'cheque':
            if not cheque:
                raise forms.ValidationError('The field is Required')
            return cheque


class DisciplineForm(forms.ModelForm):
	class Meta:
		model = Disciplines
		# template_name = "core/discipline_form.html"
		fields = ['type','fact_date' , 'student', 'status', 'created_by', 'location', 'motif', 'comment']
		

		
class DisciplineDetailsForm(forms.ModelForm):
	class Meta:
		model = Disciplines_Details
		fields = [
			'start_date',
			'start_time',
			'finish_date',
			'finish_time',
			'description'
		]
		
		widgets = {
			'description': forms.Textarea(attrs={'rows': 1}),
		}
		
DisciplineDetailsFormSet = formset_factory(DisciplineDetailsForm, extra=0)

DisciplineDetailsInlineFormSet = forms.inlineformset_factory(Disciplines, Disciplines_Details, fields = ('id','start_date','start_time','finish_date','finish_time','description'), extra=1)