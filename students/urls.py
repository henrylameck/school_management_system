from django.urls import path

from .forms import *
from . import views
from students.views import FORMS

app_name = 'students'

urlpatterns = [
    path('registration/', views.StudentRegistrationView.as_view(FORMS), name='student-registration'),
    path('get-total-fee/', views.get_fee_total, name='get_total_fee')
]
