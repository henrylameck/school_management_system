from django.urls import path, include

from .import views

app_name = "users"

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.Login.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('create-staff/', views.CreateStaff.as_view(), name='create-staff'),
    path('update-staff/<int:pk>/', views.UpdateStaff.as_view(), name='update-staff'),
    path('delete-staff/<int:pk>/', views.DeleteStaff.as_view(), name='delete-staff'),
]