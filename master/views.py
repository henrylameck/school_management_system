from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, FormView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from .models import School, AcademicSession, Semester, Department, AcademicYear
from .forms import SchoolForm, AcademicSessionForm, SemesterForm, DepartmentForm, UpdateAcademicSessionForm, AcademicYearForm

# Create your views here.
class Dashboard(TemplateView):
    template_name = 'master/dashboard.html'


class SchoolUpdate(LoginRequiredMixin, UserPassesTestMixin, FormView):
    form_class = SchoolForm
    template_name = 'master/school_update.html'

    def test_func(self):
        if self.request.user.role == 'master':
            return True

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


class AcademicSessionView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'master/academic_session.html'
    form_class = AcademicSessionForm

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['academic_sessions'] = AcademicSession.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            session_obj = form.save(commit=False)
            session_obj.created_by = request.user
            session_obj.save()

            messages.success(request, 'Success, Academic Session created', extra_tags='alert alert-success')

            return redirect(to='master:academic_sessions')

        academic_sessions = AcademicSession.objects.all()

        context = {
            'form': form,
            'academic_sessions': academic_sessions
        }

        messages.error(request, 'Errors occurred',
                       extra_tags='alert alert-danger')

        return render(request, self.template_name, context=context)


class UpdateAcademicSession(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'master/update_academic_session.html'
    form_class = UpdateAcademicSessionForm

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def post(self, request, *args, **kwargs):

        session = get_object_or_404(AcademicSession, pk=self.kwargs['pk'])

        form = self.form_class(instance=session, data=request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request, 'Success, team details updated', extra_tags='alert alert-success')

            return redirect(to='master:academic_sessions')
        else:

            context = {
                'form': self.form_class(data=request.POST, instance=session),
                'session':session
            }

            messages.error(request, 'Failed, errors occurred.',
                           extra_tags='alert alert-danger')

            return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):

        session = get_object_or_404(AcademicSession, pk=self.kwargs['pk'])

        context = {
            'form': self.form_class(instance=session),
            'session': session,
        }

        return render(request, self.template_name, context=context)


class DeleteAcademicSession(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AcademicSession
    template_name = 'master/comfirm_delete.html'

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def get_success_url(self):

        messages.success(self.request, 'Success, Academic Year deleted',
                         extra_tags='alert alert-info')

        return reverse_lazy('master:academic_sessions')


class AcademicYearView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'master/select_academic_year.html'
    form_class = AcademicYearForm

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_year'] = AcademicYear.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            session_obj = form.save(commit=False)
            session_obj.save()

            messages.success(request, 'Success, Academic Year Selected', extra_tags='alert alert-success')

            return redirect(to='master:academic_year')


        context = {
            'form': form,
        }

        messages.error(request, 'Errors occurred',
                       extra_tags='alert alert-danger')

        return render(request, self.template_name, context=context)


class CreateDepartment(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'master/create_department.html'
    form_class = DepartmentForm

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            department_obj = form.save(commit=False)
            department_obj.save()

            messages.success(request, 'Success, Department created', extra_tags='alert alert-success')

            return redirect(to='master:create-department')


        context = {
            'form': form,
        }

        messages.error(request, 'Errors occurred',
                       extra_tags='alert alert-danger')

        return render(request, self.template_name, context=context)



class DepartmentUpdate(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'master/update_department.html'
    form_class = DepartmentForm

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def post(self, request, *args, **kwargs):

        department = get_object_or_404(Department, pk=self.kwargs['pk'])

        form = self.form_class(instance=department, data=request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request, 'Success, Department details updated', extra_tags='alert alert-success')

            return redirect(to='master:create-department')
        else:

            context = {
                'form': self.form_class(data=request.POST, instance=session),
                'session':session
            }

            messages.error(request, 'Failed, errors occurred.',
                           extra_tags='alert alert-danger')

            return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):

        department = get_object_or_404(Department, pk=self.kwargs['pk'])

        context = {
            'form': self.form_class(instance=department),
            'department': department,
        }

        return render(request, self.template_name, context=context)

