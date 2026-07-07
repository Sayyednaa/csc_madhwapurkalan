from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('inquiries/', views.inquiries_list, name='dashboard_inquiries'),
    path('inquiries/<int:pk>/update/', views.update_inquiry_status, name='update_inquiry_status'),
    path('appointments/', views.appointments_list, name='dashboard_appointments'),
    path('callbacks/', views.callbacks_list, name='dashboard_callbacks'),
    path('services/', views.services_list, name='dashboard_services'),
]
