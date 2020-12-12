from django import forms

from .models import ApplicationFormSale, ApplicationFormReceive

class ApplicationSaleForm(forms.ModelForm):

    class Meta:
        model = ApplicationFormSale
        fields = ('date', 'form_number', 'serial_number','amount', 'first_name', 'middle_name', 'last_name', 'phone_number',)

class ApplicationReceivedForm(forms.ModelForm):
    
    class Meta:
        model = ApplicationFormReceive
        fields = ('date', 'application_number', 'serial_number', 'Student_name', 'gender', 'date_of_birth', 'gurdian_name', 'phone_number',)