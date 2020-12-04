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
from .models import *

def get_fee_total(request):
    reg_fee = request.GET.get('reg_fee')
    vehicle_fee = request.GET.get('vehicle_fee')

    total = int(reg_fee) + int(vehicle_fee)

    context = {
        'total': total,
    }

    return render(request, 'students/total_fee.html', context)




FORMS = [
    ('personal_detail', PersonalDetailsForm),
    ('person_contact_detail', PersonalContactDetailForm),
    ('transport_allocation', TransportAllocationForm),
    ('hostel_allocation', HostelAllocationForm),
    ('qualification', QualificationForm),
    ('fee_collection', FeeCollectionForm)
]

TEMPLATES = {
    'personal_detail': 'students/personal_detail.html',
    'person_contact_detail': 'students/personal_contact_detail.html',
    'transport_allocation': 'students/transport_allocation.html',
    'hostel_allocation': 'students/add_student.html',
    'qualification': 'students/add_student.html',
    'fee_collection': 'students/fee_collection.html',
}


class StudentRegistrationView(SessionWizardView):
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'student_passport'))

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        if self.steps.current == 'personal_detail':
            context.update({'another_var': 'Student Details'})
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

        personal_details_instance = PersonalDetails()
        personal_contact_instance = PersonalContactDetail()
        transport_allocation_instance = TransportAllocation()
        hostel_allocation_instance = HostelAllocation()
        qualification_instance = Qualification()
        fee_collection_instance = FeeCollection()
        student_registration_instance = StudentRegistration()

        student_registration_instance.created_by = self.request.user

        student_registration_instance.personal_details = personal_details_instance

        student_registration_instance.personal_contact_detail = personal_contact_instance

        student_registration_instance.transport_allocation = transport_allocation_instance

        student_registration_instance.hostel_allocation = hostel_allocation_instance

        student_registration_instance.qualification = qualification_instance

        student_registration_instance.feecollection = fee_collection_instance

        for form in form_list:

            personal_details_instance = construct_instance(form, personal_details_instance, form._meta.fields, form._meta.exclude)

            personal_contact_instance = construct_instance(form, personal_contact_instance, form._meta.fields, form._meta.exclude)

            transport_allocation_instance = construct_instance(form, transport_allocation_instance, form._meta.fields, form._meta.exclude)

            hostel_allocation_instance = construct_instance(form, hostel_allocation_instance, form._meta.fields, form._meta.exclude)

            qualification_instance = construct_instance(form, qualification_instance, form._meta.fields, form._meta.exclude)

            fee_collection_instance = construct_instance(form, fee_collection_instance, form._meta.fields, form._meta.exclude)

            student_registration_instance = construct_instance(form, student_registration_instance, form._meta.fields, form._meta.exclude)

        personal_details_instance.save()
        personal_contact_instance.save()
        transport_allocation_instance.save()
        hostel_allocation_instance.save()
        qualification_instance.save()
        fee_collection_instance.save()
        student_registration_instance.save()

        return render(self.request, 'students/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)
