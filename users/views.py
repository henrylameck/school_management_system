from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage
from django.views.generic import TemplateView, FormView, DeleteView
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, PermissionDenied
from django.contrib.auth import get_user_model

from .forms import SignUpForm, CreateStaffForm, UpdateStaffForm
from .models import Profile
from master.models import School


User = get_user_model()

BASE_URL = 'http://127.0.0.1:8000'


class Login(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        if url:
            return url
        elif self.request.user.role == 'master':
            return reverse('master:dashboard')
        elif self.request.user.role == 'teacher':
            return reverse('/')
        elif self.request.user.role == 'secretary':
            return reverse('/')
        elif self.request.user.role == 'accountant':
            return reverse('/')
        elif self.request.user.role == 'hr':
            return reverse('/')
        elif self.request.user.role == 'librarian':
            return reverse('/')
        elif self.request.user.role == 'academy':
            return reverse('/')
        elif self.request.user.role == 'matron':
            return reverse('/')
        elif self.request.user.role == 'vehicle':
            return reverse('/')
        else:
            return f'admin'


class SignUp(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'users/signup.html'
    form_class = SignUpForm
    permission_denied_message = 'Only Superuser has access to this page'

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save()
            user.save()

            # create profile
            profile = Profile(user=user)
            profile.save()

            #create school
            school = School(master=user)
            school.save()

            return redirect('users:login')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class LogoutView(LogoutView):
    template_name = 'registration/logout.html'


class CreateStaff(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'users/create_staff.html'
    form_class = CreateStaffForm
    permission_denied_message = 'Only Master has access to this page'

    def test_func(self):
        if self.request.user.role == 'master':
            return True


    def get(self, request, *args, **kwargs):

        staffs = User.objects.filter(created_by=self.request.user).order_by('-pk')

        context = {
            'form': self.form_class,
            'staffs': staffs
        }

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():

            staff_obj = form.save(commit=False)
            staff_obj.created_by = self.request.user

            # Set default password
            staff_password = get_random_string(length=8)
            staff_obj.set_password(
                raw_password=staff_password
            )
            staff_obj.save()

            # create profile
            profile = Profile(user=staff_obj)
            profile.save()

            #send Login credentials to team member email
            staff_email = form.cleaned_data['email']
            message = get_template(
                'users/login_credentials_email.html').render(
                {
                    'email': staff_email,
                    'password':staff_password
                    })
            mail = EmailMessage(
                'ShuleCom login Credentials',
                message,
                to=[staff_email],
                from_email=settings.EMAIL_HOST_USER)
            mail.content_subtype = 'html'
            mail.send()

            messages.success(request, 'Success, Staff created',
                             extra_tags='alert alert-success')

            return redirect(to='users:create-staff')

        staffs = User.objects.filter(created_by=self.request.user).order_by('-pk')

        context = {
            'form': form,
            'staffs': staffs
        }

        messages.error(request, 'Errors occurred',
                       extra_tags='alert alert-danger')

        return render(request, self.template_name, context=context)



class UpdateStaff(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'users/edit_staff.html'
    form_class = UpdateStaffForm
    permission_denied_message = 'Only Master has access to this page'

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def post(self, request, *args, **kwargs):

        staff = get_object_or_404(User, pk=self.kwargs['pk'])

        form = self.form_class(instance=staff, data=request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request, 'Success, staff details updated', extra_tags='alert alert-success')

            return redirect(to='users:update-staff', pk=self.kwargs['pk'])
        else:

            context = {
                'form': self.form_class(data=request.POST, instance=staff),
                'staff': staff,
            }

            messages.error(request, 'Failed, errors occurred.',
                           extra_tags='alert alert-danger')

            return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):

        staff = get_object_or_404(User, pk=self.kwargs['pk'])

        context = {
            'form': self.form_class(instance=staff),
            'staff': staff,
        }

        return render(request, self.template_name, context=context)


class DeleteStaff(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/comfirm_delete.html'
    permission_denied_message = 'Only Master has access to this page'

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def get_success_url(self):

        messages.success(self.request, 'Success, staff deleted',
                         extra_tags='alert alert-info')

        return reverse_lazy('users:create-staff')
