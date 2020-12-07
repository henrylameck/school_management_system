from django.urls import path

from .import views

app_name='classes'

urlpatterns = [
    path('list/', views.classes_syllabus_list, name='class_list'),
    
    path('create-stream/', views.CreateStream.as_view(), name='create-stream'),
    path('stream/<int:pk>/delete/', views.DeleteStream.as_view(), name='delete-stream'),

    path('create-subject/', views.CreateSubject.as_view(), name='create-subject'),
    
    path('subject/<int:pk>/delete/', views.DeleteSubject.as_view(), name='delete-subject'),

    path('syllabus/<int:id>/edit/', views.create_edit_class, name='edit_syllabus'),

    path('create-class/', views.create_edit_class, name='class-syllabus')
]
