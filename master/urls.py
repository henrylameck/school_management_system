from django.urls import path

from .import views

app_name = 'master'

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('school/<int:pk>/edit/', views.SchoolUpdate.as_view(), name='school-edit'),
]