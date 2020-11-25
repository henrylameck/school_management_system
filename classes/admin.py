from django.contrib import admin

from .models import Stream, Class, Subject, ClassSyllabus

admin.site.register(Stream)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(ClassSyllabus)

# Register your models here.
