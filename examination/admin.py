from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ExamMaster)
admin.site.register(ExamSubject)
admin.site.register(ExamDivision)
admin.site.register(ExamGrade)
admin.site.register(ExamMarkMaster)
admin.site.register(ExamMarkEntry)
admin.site.register(ExamMarkEntryPart)
