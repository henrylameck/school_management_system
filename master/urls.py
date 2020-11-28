from django.urls import path

from .import views

app_name = 'master'

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('school/<int:pk>/edit/', views.SchoolUpdate.as_view(), name='school-edit'),
    path('academic_sessions/', views.AcademicSessionView.as_view(), name='academic_sessions'),
    path('academic-update/<int:pk>/', views.UpdateAcademicSession.as_view(), name='academic-session-update'),
    path('academic-session/<int:pk>/delete/', views.DeleteAcademicSession.as_view(), name='delete-academic-session'),
    path('select-academic-year/', views.AcademicYearView.as_view(), name='academic_year'),
    path('create-department/', views.CreateDepartment.as_view(), name='create-department'),
    path('update-department/<int:pk>/', views.DepartmentUpdate.as_view(), name='update-department')
]