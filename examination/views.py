from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .resources import ExamMarkEntryResource
from .models import *
from students.models import StudentAdmission
from .forms import ExamSubjectInlineFormSet, ExamMasterForm


def export(request):
    classes = Class.objects.all()
    subjects = Subject.objects.all()
    exams = ExamMaster.objects.all()

    if request.method == 'POST':
        select_class = request.POST.get('select_class')
        subject = request.POST.get('subject')
        exam_name = request.POST.get('exam')
        semister = request.POST.get('semister')

        exam_resource = ExamMarkEntryResource()
        dataset = exam_resource.export(
            ExamMarkEntry.objects.filter(
                exam_master__select_class=select_class,
                exam_subject__subject_id=subject,
                exam_master__name=exam_name,
                exam_master__select_term=semister,
                created_by=request.user,
            )
        )

        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="exam.csv"'
        return response

    context = {
        'classes':classes,
        'subjects':subjects,
        'exams':exams,
    }
    return render(request, 'examination/export_exam.html', context)



@login_required
def create_edit_exam(request, id=None):
    """
        This is an inline formset to create a new exam entry along with exam subjects that can have multiple occurences.
    """

    user = request.user

    if id: 
        exam_master = get_object_or_404(ExamMaster, id=id)
        exam_subject = ExamSubject.objects.filter(exam_master=exam_master)
        formset = ExamSubjectInlineFormSet(instance=exam_master)
        if exam_master.created_by != request.user:
            return HttpResponseForbidden()
    else:
        exam_master = ExamMaster(created_by=user)
        formset = ExamSubjectInlineFormSet(instance=exam_master)

    if request.POST:

        form = ExamMasterForm(request.POST, instance=exam_master)

        formset = ExamSubjectInlineFormSet(request.POST or None,prefix='exam_subject')

        if form.is_valid():
            exam_form = form.save(commit=False)

            classe = exam_form.select_class

            students = StudentAdmission.objects.filter(class_name=classe)
            
            if id:
                exam_form.last_user = user
            formset = ExamSubjectInlineFormSet(request.POST,prefix='exam_subject',instance=exam_form)

            if formset.is_valid():
                exam_form.save()

                exam_subject = formset.save(commit=False)
                for e in exam_subject:
                    if id:
                        e.last_user = user
                    else: e.created_by = user
                    e.save()

                    exam_form_id = exam_form.id
                    exam_subject_id = e.id

                    for student in students:

                        exam_mark = ExamMarkEntry.objects.create(
                            exam_master_id = exam_form_id,
                            created_by = request.user,
                            student = student,
                            exam_subject_id = exam_subject_id,
                        )

                return redirect('examination:exam_list')
            else: 
                print("formset not valid")
                print("error ", formset.errors)
                print("non form error ", formset.non_form_errors())
        else: print("form not valid")
    else:
        form = ExamMasterForm(instance=exam_master)
        formset = ExamSubjectInlineFormSet(instance=exam_master, prefix='exam_subject')

    variables = {
        'form': form,
        'formset': formset
    }

    template = 'examination/exam_subjects.html'

    return render(request, template, variables)


