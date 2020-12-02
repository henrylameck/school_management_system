from django import forms

from .models import PersonalDetails, StudentAdmission, PersonalContactDetail, TransportAllocation, HostelAllocation, Qualification,FeeCollection


class PersonalDetailsForm(forms.ModelForm):

    class Meta:
        model = PersonalDetails
        exclude = ['created_by',]


class StudentAdmissionForm(forms.ModelForm):

    class Meta:
        model = StudentAdmission
        exclude = ['created_by',]


class PersonalContactDetailForm(forms.ModelForm):

    class Meta:
        model = PersonalContactDetail
        exclude = ['created_by',]


class TransportAllocationForm(forms.ModelForm):

    class Meta:
        model = TransportAllocation
        exclude = ['created_by',]


class HostelAllocationForm(forms.ModelForm):

    class Meta:
        model = HostelAllocation
        exclude = ['created_by',]


class QualificationForm(forms.ModelForm):

    class Meta:
        model = Qualification
        exclude = ['created_by',]


class FeeCollectionForm(forms.ModelForm):

    class Meta:
        model = FeeCollection
        exclude = ['created_by',]