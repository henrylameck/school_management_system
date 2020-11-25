from django.contrib import admin
from .models import School, Department, AcademicSession, Semester

# Register your models here.
admin.site.register(School)
admin.site.register(Department)
admin.site.register(AcademicSession)
admin.site.register(Semester)
