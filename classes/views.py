from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden, HttpResponseRedirect, Http404
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, FormView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy, reverse

from .models import Class, Stream, Subject, ClassSyllabus
from .forms import ClassForm, StreamForm, SubjectForm, ClassSyllabusForm, ClassSyllabusInlineFormSet




class CreateStream(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'classes/create_stream.html'
    form_class = StreamForm

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['streams'] = Stream.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            stream_obj = form.save(commit=False)
            stream_obj.created_by = request.user
            stream_obj.save()

            messages.success(request, 'Success, Stream was created', extra_tags='alert alert-success')

            return redirect(to='classes:create-stream')


        context = {
            'form': form,
        }

        messages.error(request, 'Errors occurred',
                       extra_tags='alert alert-danger')

        return render(request, self.template_name, context=context)


class DeleteStream(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Stream
    template_name = 'master/comfirm_delete.html'

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def get_success_url(self):

        messages.success(self.request, 'Success, Stream deleted',
                         extra_tags='alert alert-info')

        return reverse_lazy('classes:create-stream')


class CreateSubject(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'classes/create_subject.html'
    form_class = SubjectForm

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            subject_obj = form.save(commit=False)
            subject_obj.created_by = request.user
            subject_obj.save()

            messages.success(request, 'Success, Subject was created', extra_tags='alert alert-success')

            return redirect(to='classes:create-subject')


        context = {
            'form': form,
        }

        messages.error(request, 'Errors occurred',
                       extra_tags='alert alert-danger')

        return render(request, self.template_name, context=context)


class DeleteSubject(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Subject
    template_name = 'master/comfirm_delete.html'

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def get_success_url(self):

        messages.success(self.request, 'Success, Stream deleted',
                         extra_tags='alert alert-info')

        return reverse_lazy('classes:create-subject')


class CreateClassSyllabus(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'classes/create_syllabus.html'
    form_class = ClassSyllabusForm

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['syllabus'] = ClassSyllabus.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            syllabus_obj = form.save(commit=False)
            syllabus_obj.created_by = request.user
            syllabus_obj.save()

            messages.success(request, 'Success, Class Syllabus was created', extra_tags='alert alert-success')

            return redirect(to='classes:create-syllabus')


        context = {
            'form': form,
        }

        messages.error(request, 'Errors occurred',
                       extra_tags='alert alert-danger')

        return render(request, self.template_name, context=context)


class DeleteSyllabus(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ClassSyllabus
    template_name = 'master/comfirm_delete.html'

    def test_func(self):
        if self.request.user.role == 'master':
            return True

    def get_success_url(self):

        messages.success(self.request, 'Success, Class Syllabus deleted',
                         extra_tags='alert alert-info')

        return reverse_lazy('classes:create-syllabus')


def class_list(request):
    classes = Class.objects.all()
    return render(request, 'classes/class_list.html', {'classes': classes})


def save_class_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            class_obj = form.save(commit=False)
            class_obj.created_by = request.user
            class_obj.save()
            data['form_is_valid'] = True
            classes = Class.objects.all()
            data['html_class_list'] = render_to_string('classes/includes/partial_class_list.html', {
                'classes': classes
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 

def class_create(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
    else:
        form = ClassForm()
    return save_class_form(request, form, 'classes/includes/partial_class_create.html')


def class_update(request, pk):
    class_s = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=class_s)
    else:
        form = ClassForm(instance=class_s)
    return save_class_form(request, form, 'classes/includes/partial_class_update.html')


def class_delete(request, pk):
    class_s = get_object_or_404(Class, pk=pk)
    data = dict()
    if request.method == 'POST':
        class_s.delete()
        data['form_is_valid'] = True
        classes = Class.objects.all()
        data['html_class_list'] = render_to_string('classes/includes/partial_class_list.html', {
            'classes': classes
        })
    else:
        context = {'class_s': class_s}
        data['html_form'] = render_to_string('classes/includes/partial_class_delete.html', context, request=request)
    return JsonResponse(data)


def is_valid_queryparam(param):
    return param != '' and param is not None


@login_required
def classes_syllabus_list(request):
    classes_syllabus = ClassSyllabus.objects.all()
    classes = Class.objects.all()
    classe = request.POST.get('classe')

    if is_valid_queryparam(classe) and classe != 'Choose class':
        classes_syllabus = classes_syllabus.filter(select_class__id=classe)

    context = {
        'classes':classes,
        'classes_syllabus':classes_syllabus
    }

    template = 'classes/class_list.html'

    return render(request, template, context)


@login_required
def create_edit_class(request, id=None):
    """
        This is an inline formset to create a new class entry along with class syllabus that can have multiple occurences.
    """

    user = request.user

    if id: 
        classes = get_object_or_404(Class, id=id)
        print('classes:', classes)
        class_syllabus = ClassSyllabus.objects.filter(select_class=classes)
        formset = ClassSyllabusInlineFormSet(instance=classes)
        if classes.created_by != request.user:
            return HttpResponseForbidden()
    else:
        classes = Class(created_by=user)
        formset = ClassSyllabusInlineFormSet(instance=classes)

    if request.POST:
        form = ClassForm(request.POST, instance=classes)
        formset = ClassSyllabusInlineFormSet(request.POST or None,prefix='class_syllabus')
        if form.is_valid():
            class_form = form.save(commit=False)
            if id:
                class_form.last_user = user
            formset = ClassSyllabusInlineFormSet(request.POST,prefix='class_syllabus',instance=class_form)
            if formset.is_valid():
                class_form.save()
                class_syllabus = formset.save(commit=False)
                for e in class_syllabus:
                    if id:
                        e.last_user = user
                    else: e.created_by = user
                    e.save()
                return redirect('classes:class-syllabus')
            else: 
                print("formset not valid")
                print("error ", formset.errors)
                print("non form error ", formset.non_form_errors())
        else: print("form not valid")
    else:
        form = ClassForm(instance=classes)
        formset = ClassSyllabusInlineFormSet(instance=classes, prefix='class_syllabus')

    variables = {
        'form': form,
        'formset': formset
    }

    template = 'classes/class_syllabus.html'

    return render(request, template, variables)
	