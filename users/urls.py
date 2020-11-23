from django.urls import path, include

from .import views

app_name = "users"

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('create/', views.CreateStaff.as_view(), name='create-staff'),
    path('update/<int:pk>/', views.UpdateStaff.as_view(), name='update-staff'),
    path('delete-staff/<int:pk>/', views.DeleteStaff.as_view(), name='delete-staff'),
]