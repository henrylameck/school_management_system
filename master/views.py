from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy, reverse
from django.contrib import messages

from .models import School
from .forms import SchoolForm

# Create your views here.
class Dashboard(TemplateView):
    template_name = 'master/dashboard.html'


class SchoolUpdate(FormView):
    form_class = SchoolForm
    template_name = 'master/school_update.html'

    # def get_success_url(self):
    #     messages.success(
    #             request, 'Success, team details updated', extra_tags='alert alert-success')
    #     return reverse('master:school-edit', kwargs={'pk':self.object.id})


    def post(self, request, *args, **kwargs):

        school = get_object_or_404(School, pk=self.kwargs['pk'])

        form = self.form_class(instance=school, data=request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request, 'Success, School details updated', extra_tags='alert alert-success')

            return redirect(to='master:school-edit', pk=self.kwargs['pk'])
        else:

            context = {
                'form': self.form_class(data=request.POST, instance=school),
                'school':school
            }

            messages.error(request, 'Failed, errors occurred.',
                           extra_tags='alert alert-danger')

            return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):

        school = get_object_or_404(School, pk=self.kwargs['pk'])

        context = {
            'form': self.form_class(instance=school),
            'school':school
        }

        return render(request, self.template_name, context=context)
