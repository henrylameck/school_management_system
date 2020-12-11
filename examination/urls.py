from django.urls import path

from .import views

app_name = 'examination'

urlpatterns = [
    path('export/', views.export, name='export'),
    path('create-edit/',views.create_edit_exam, name='exam-create-edit'),
]