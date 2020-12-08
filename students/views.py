import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.forms import modelformset_factory
from django.contrib import messages
from django.forms.models import construct_instance
from django.contrib.auth.decorators import login_required

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


def student_list(request):
    students = StudentAdmission.objects.all().order_by('-created_at')
    return render(request, 'students/student_list.html', {'students': students})


def save_student_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            student_obj = form.save(commit=False)
            student_obj.created_by = request.user
            student_obj.save()
            data['form_is_valid'] = True
            students = StudentAdmission.objects.all()
            data['html_student_list'] = render_to_string('students/includes/partial_student_list.html', {
                'students': students
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def student_create(request):
    if request.method == 'POST':
        form = StudentAdmissionForm(request.POST)
    else:
        form = StudentAdmissionForm()
    return save_student_form(request, form, 'students/includes/partial_student_create.html')


@login_required
def create_edit_discipline(request, id=None):
	"""
		This is an inline formset to create a new discipline entry along with discipline details that can have multiple occurences.
	"""
 
	user = request.user
	
	if id: 
		discipline = get_object_or_404(Disciplines, id=id)
		discipline_details = Disciplines_Details.objects.filter(discipline=discipline)
		formset = DisciplineDetailsInlineFormSet(instance=discipline)
		if discipline.created_by != request.user:
			return HttpResponseForbidden()
	else:
		discipline = Disciplines(created_by=user)
		formset = DisciplineDetailsInlineFormSet(instance=discipline)
	
	if request.POST:
		form = DisciplineForm(request.POST, instance=discipline)
		formset = DisciplineDetailsInlineFormSet(request.POST,prefix='discipline_detail')
		if form.is_valid():
			discipline_form = form.save(commit=False)
			if id:
				discipline_form.last_user = user
			formset = DisciplineDetailsInlineFormSet(request.POST,prefix='discipline_detail',instance=discipline_form)
			if formset.is_valid():
				discipline_form.save()
				discipline_details = formset.save(commit=False)
				for e in discipline_details:
					if id:
						e.last_user = user
					else: e.created_by = user
					e.save()
				return redirect('students:disciplines_list')
			else: 
				print("formset not valid")
				print("error ", formset.errors)
				print("non form error ", formset.non_form_errors())
		else: print("form not valid")
	else:
		form = DisciplineForm(instance=discipline)
		formset = DisciplineDetailsInlineFormSet(instance=discipline, prefix='discipline_detail')
	
	variables = {
		'form': form,
		'formset': formset
	}
	
	template = 'students/disciplines/discipline_form.html'

	return render(request, template, variables)


@login_required
def disciplines_list(request):
	classe_obj_list = Class.objects.all()
	student_obj_list = StudentAdmission.objects.filter(class_name__in=classe_obj_list)
	disciplines_obj_list = Disciplines.objects.filter(student__in=student_obj_list)
	disciplines_type_obj_list = Discipline_type.objects.all().only('sanction') # get all discipline types
	
	discipline_type_filter = request.POST.get('sanction')
	student_fname_filter = request.POST.get('fname')
	student_lname_filter = request.POST.get('lname')
	student_classe_filter = request.POST.get('classe')
	fact_date_filter = request.POST.get('fact_date')
	
	# Setup of the form filter id="discipline_list_filter" in student/templates/disciplines.html 
	if discipline_type_filter:
		disciplines_obj_list = disciplines_obj_list.filter(type__id=discipline_type_filter)
	if student_fname_filter:
		disciplines_obj_list = disciplines_obj_list.filter(student__student__personal_details__first_name__icontains=student_fname_filter)
	if student_lname_filter :
		disciplines_obj_list = disciplines_obj_list.filter(student__student__personal_details__last_name__icontains=student_lname_filter)
	if student_classe_filter:
		disciplines_obj_list = disciplines_obj_list.filter(student__class_name__id=student_classe_filter)
	if fact_date_filter:
		disciplines_obj_list = disciplines_obj_list.filter(fact_date=fact_date_filter)
	
	variables = {
		'disciplines_obj_list': disciplines_obj_list, 
		'classe_obj_list':classe_obj_list, 
		'disciplines_type_obj_list':disciplines_type_obj_list, 
	}
	
	template = 'students/disciplines/disciplines.html'
	
	return render(request, template, variables)