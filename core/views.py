from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, ServiceCategory, WebsiteContent, FAQ, Inquiry, CallbackRequest, Appointment

def get_global_context():
    content = WebsiteContent.objects.first()
    return {'site_content': content}

def home(request):
    context = get_global_context()
    context['popular_services'] = Service.objects.filter(is_active=True)[:12]
    return render(request, 'core/home.html', context)

def about(request):
    context = get_global_context()
    return render(request, 'core/about.html', context)

def services(request):
    context = get_global_context()
    categories = ServiceCategory.objects.prefetch_related('services').all()
    context['categories'] = categories
    return render(request, 'core/services.html', context)

def faq(request):
    context = get_global_context()
    context['faqs'] = FAQ.objects.filter(is_active=True)
    return render(request, 'core/faq.html', context)

def contact(request):
    context = get_global_context()
    if request.method == 'POST':
        # Simple processing for contact form mapping to inquiry for now
        name = request.POST.get('name')
        mobile = request.POST.get('mobile_number')
        email = request.POST.get('email', '')
        message = request.POST.get('message')
        
        if name and mobile and message:
            Inquiry.objects.create(
                name=name,
                mobile_number=mobile,
                email=email,
                message=message
            )
            messages.success(request, 'Your message has been sent successfully. We will contact you soon.')
            return redirect('contact')
            
    return render(request, 'core/contact.html', context)
