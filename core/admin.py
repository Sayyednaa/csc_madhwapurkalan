from django.contrib import admin
from .models import ServiceCategory, Service, Inquiry, Appointment, CallbackRequest, WebsiteContent

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    search_fields = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active', 'estimated_processing_time')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_number', 'service_interested', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'mobile_number', 'email')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_number', 'service', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('name', 'mobile_number')

@admin.register(CallbackRequest)
class CallbackRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_number', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'mobile_number')

@admin.register(WebsiteContent)
class WebsiteContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_phone')
