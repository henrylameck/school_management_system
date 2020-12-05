from django.urls import path

from .import views

app_name='classes'

urlpatterns = [
    path('list/', views.class_list, name='class_list'),
    path('create/', views.class_create, name='class_create'),
    path('<int:pk>/update/', views.class_update, name='class_update'),
    path('<int:pk>/delete/', views.class_delete, name='class_delete'),
    path('create-stream/', views.CreateStream.as_view(), name='create-stream'),
    path('stream/<int:pk>/delete/', views.DeleteStream.as_view(), name='delete-stream'),
    path('create-subject/', views.CreateSubject.as_view(), name='create-subject'),
    path('subject/<int:pk>/delete/', views.DeleteSubject.as_view(), name='delete-subject'),
    path('create-syllabus/', views.CreateClassSyllabus.as_view(), name='create-syllabus'),
    path('syllabus/<int:pk>/delete/', views.DeleteSyllabus.as_view(), name='delete-syllabus')
]
