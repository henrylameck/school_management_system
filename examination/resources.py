from import_export import resources
from import_export.fields import Field

from .models import ExamMarkEntry


class ExamMarkEntryResource(resources.ModelResource):
    student_name = Field(attribute='student__student', column_name='STUDENT', readonly=True)
    theory_mark = Field(attribute='theory_mark', column_name='THEORY MARK',)
    assignment_mark = Field(attribute='assignment_mark', column_name='ASSIGNMENT MARK',)
    practical_mark = Field(attribute='practical_mark', column_name='PRACTICAL MARK',)
    project_mark = Field(attribute='project_mark', column_name='PROJECT MARK',)

    class Meta:
        model = ExamMarkEntry
        skip_unchanged = True
        report_skipped = False
        fields = ()
        export_order = ('student_name','theory_mark', 'assignment_mark', 'practical_mark', 'project_mark',)