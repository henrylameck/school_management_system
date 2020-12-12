from django.urls import path

from .forms import *
from . import views
from students.views import FORMS

app_name = 'students'

urlpatterns = [
    path('registration/', views.StudentRegistrationView.as_view(FORMS), name='student-registration'),
    path('get-total-fee/', views.get_fee_total, name='get_total_fee'),
    path('admission/', views.student_list, name='student_list'),
    path('create/admission/', views.student_create, name='student_create'),

    path('disciplines/', views.disciplines_list, name='disciplines_list'),
	# path('<int:id>/details/', views.discipline_details, name='discipline_details'),
	path('discipline/create/', views.create_edit_discipline, name='create_discipline'), 
	path('discipline/<int:id>/edit/', views.create_edit_discipline, name='edit_discipline'), 
	# path('discipline/<int:id>/delete/', views.delete_discipline, name='delete_discipline'),
]
