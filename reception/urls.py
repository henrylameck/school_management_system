from django.urls import path

from .import views

app_name='reception'

urlpatterns = [
    path('create-application-form_sale/', views.CreateApplicationFormSale.as_view(), name='create-application-form-sale'),
    path('applicationformsale/<int:pk>/delete/', views.DeleteApplicationForm.as_view(), name='delete-application-form'),
    path('application-form-received/', views.ApplicationReceive.as_view(), name='application-form-received'),
    # path('load-application-details/', views.load_application_received_details, name='ajax_load_logos'),
]
