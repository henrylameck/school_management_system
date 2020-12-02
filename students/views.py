import os
from django.shortcuts import render
from django.urls import reverse
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.forms import modelformset_factory
from django.contrib import messages
from django.forms.models import construct_instance

from .forms import *


FORMS = [
    ('student_admission', StudentAdmissionForm),
    ('personal_detail', PersonalDetailsForm),
    ('person_contact_detail', PersonalContactDetailForm),
    ('transport_allocation', TransportAllocationForm),
    ('hostel_allocation', HostelAllocationForm),
    ('qualification', QualificationForm),
    ('fee_collection', FeeCollectionForm)
]

TEMPLATES = {
    'personal_detail': 'students/add_student.html',
    'student_admission': 'students/add_student.html',
    'person_contact_detail': 'students/add_student.html',
    'transport_allocation': 'students/add_student.html',
    'hostel_allocation': 'students/add_student.html',
    'qualification': 'students/add_student.html',
    'fee_collection': 'students/add_student.html',
}


class StudentRegistrationView(SessionWizardView):
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'student_passport'))

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        if self.steps.current == 'student_admission':
            context.update({'another_var': 'Student admission'})
        elif self.steps.current == 'personal_detail':
            context.update({'another_var': 'Personal Details'})
        elif self.steps.current == 'person_contact_detail':
            context.update({'another_var': 'Personal Contact Details'})
        elif self.steps.current == 'transport_allocation':
            context.update({'another_var': 'Transport Allocation'})
        elif self.steps.current == 'hostel_allocation':
            context.update({'another_var': 'Hostel Allocation'})
        elif self.steps.current == 'qualification':
            context.update({'another_var': 'Qualification'})
        elif self.steps.current == 'fee_collection':
            context.update({'another_var': 'Fee Collection'})
        return context

    def done(self, form_list, **kwargs):

        student_admission_instance = StudentAdmission()
        personal_details_instance = PersonalDetails()
        personal_contact_instance = PersonalContactDetail()
        transport_allocation_instance = TransportAllocation()
        hostel_allocation_instance = HostelAllocation()
        qualification_instance = Qualification()
        fee_collection_instance = FeeCollection()

        student_admission_instance.created_by = self.request.user
        personal_details_instance.created_by = self.request.user
        personal_contact_instance.created_by = self.request.user
        transport_allocation_instance.created_by = self.request.user
        hostel_allocation_instance.created_by = self.request.user
        qualification_instance.created_by = self.request.user
        fee_collection_instance.created_by = self.request.user

        for form in form_list:
            student_admission_instance = construct_instance(form, student_admission_instance, form._meta.fields, form._meta.exclude)

            personal_details_instance = construct_instance(form, personal_details_instance, form._meta.fields, form._meta.exclude)

            personal_contact_instance = construct_instance(form, personal_contact_instance, form._meta.fields, form._meta.exclude)

            transport_allocation_instance = construct_instance(form, transport_allocation_instance, form._meta.fields, form._meta.exclude)

            hostel_allocation_instance = construct_instance(form, hostel_allocation_instance, form._meta.fields, form._meta.exclude)

            qualification_instance = construct_instance(form, qualification_instance, form._meta.fields, form._meta.exclude)

            fee_collection_instance = construct_instance(form, fee_collection_instance, form._meta.fields, form._meta.exclude)

        student_admission_instance.save()
        personal_details_instance.save()
        personal_contact_instance.save()
        transport_allocation_instance.save()
        hostel_allocation_instance.save()
        qualification_instance.save()
        fee_collection_instance.save()

        return render(self.request, 'students/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)
