from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from core.models import Inquiry, Appointment, CallbackRequest, Service, ServiceCategory, WebsiteContent
from django.utils import timezone

@staff_member_required
def dashboard_home(request):
    today = timezone.now().date()
    
    context = {
        'total_inquiries': Inquiry.objects.count(),
        'today_inquiries': Inquiry.objects.filter(created_at__date=today).count(),
        'pending_appointments': Appointment.objects.filter(status='PENDING').count(),
        'pending_callbacks': CallbackRequest.objects.filter(status='PENDING').count(),
        'recent_inquiries': Inquiry.objects.all()[:5],
    }
    return render(request, 'dashboard/home.html', context)

@staff_member_required
def inquiries_list(request):
    status_filter = request.GET.get('status', '')
    inquiries = Inquiry.objects.all()
    
    if status_filter:
        inquiries = inquiries.filter(status=status_filter)
        
    context = {
        'inquiries': inquiries,
        'current_status': status_filter,
        'statuses': Inquiry.STATUS_CHOICES,
    }
    return render(request, 'dashboard/inquiries.html', context)

@staff_member_required
def update_inquiry_status(request, pk):
    if request.method == 'POST':
        inquiry = get_object_or_404(Inquiry, pk=pk)
        new_status = request.POST.get('status')
        if new_status in dict(Inquiry.STATUS_CHOICES):
            inquiry.status = new_status
            inquiry.save()
            messages.success(request, f'Inquiry #{inquiry.id} status updated to {new_status}.')
    return redirect('dashboard_inquiries')

@staff_member_required
def appointments_list(request):
    context = {
        'appointments': Appointment.objects.all(),
    }
    return render(request, 'dashboard/appointments.html', context)

@staff_member_required
def callbacks_list(request):
    context = {
        'callbacks': CallbackRequest.objects.all(),
    }
    return render(request, 'dashboard/callbacks.html', context)

@staff_member_required
def services_list(request):
    context = {
        'services': Service.objects.select_related('category').all(),
    }
    return render(request, 'dashboard/services.html', context)
