from django.shortcuts import render, get_object_or_404, redirect
import os
from django.template.loader import render_to_string
from django.urls import reverse
from formtools.wizard.views import SessionWizardView
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.forms import modelformset_factory
from django.contrib import messages
from django.forms.models import construct_instance
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, FormView, CreateView, DeleteView

from .forms import ApplicationSaleForm, ApplicationReceivedForm
from .models import ApplicationFormSale, ApplicationFormReceive


class CreateApplicationFormSale(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'reception/create_application_form_sale.html'
    form_class = ApplicationSaleForm

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ApplicationFormSale'] = ApplicationFormSale.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            subject_obj = form.save(commit=False)
            subject_obj.created_by = request.user
            subject_obj.save()

            messages.success(request, 'Success, Application Form sold was created', extra_tags='alert alert-success')

            return redirect(reverse('reception:create-application-form-sale'))


        context = {
            'form': form,
        }

        messages.error(request, 'Errors occurred', extra_tags='alert alert-danger')

        return render(request, self.template_name, context=context)


class DeleteApplicationForm(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ApplicationFormSale
    template_name = 'master/comfirm_delete.html'

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def get_success_url(self):

        messages.success(self.request, 'Success, Application Form Deleted',
                         extra_tags='alert alert-info')

        return reverse_lazy('reception:create-application-form-sale')

class ApplicationReceive(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'reception/application_form_received.html'
    form_class = ApplicationReceivedForm

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ApplicationReceived'] = ApplicationFormReceive.objects.all()
        return context


    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            application_form_obj = form.save(commit=False)
            application_form_obj.created_by = request.user
            application_form_obj.save()

            messages.success(request, 'Success, Application Form was Reveived', extra_tags='alert alert-success')

            return redirect(reverse('reception:application-form-received'))


        context = {
            'form': form,
        }

        messages.error(request, 'Errors occurred', extra_tags='alert alert-danger')

        return render(request, self.template_name, context=context)


    # def load_application_received_details(request):
    #     ApplicationFormSale_id = request.GET.get('ApplicationFormSale')
    #     if ApplicationFormSale_id == '':
    #         ApplicationFormSale_id = ApplicationFormReceive.objects.get(id=1)
    #     else:
    #         ApplicationFormSale_id = ApplicationFormSale.objects.get(id=ApplicationFormSale_id)
        
    #     return render(request, 'reception/application_form_received.html', {'ApplicationFormSale_id': ApplicationFormSale})