from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = 'Service Categories'
        ordering = ['order', 'name']
        
    def __str__(self):
        return self.name

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=200)
    description = models.TextField()
    required_documents = models.TextField(blank=True)
    estimated_processing_time = models.CharField(max_length=100, blank=True)
    icon = models.ImageField(upload_to='service_icons/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order', 'name']
        
    def __str__(self):
        return self.name

class Inquiry(models.Model):
    STATUS_CHOICES = (
        ('NEW', 'New'),
        ('CONTACTED', 'Contacted'),
        ('CLOSED', 'Closed'),
    )
    
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    service_interested = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    document = models.FileField(upload_to='inquiry_docs/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.service_interested}"

class CallbackRequest(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('CALLED', 'Called'),
        ('COMPLETED', 'Completed'),
    )
    
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    preferred_time = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.mobile_number}"

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
        ('RESCHEDULED', 'Rescheduled'),
        ('COMPLETED', 'Completed'),
    )
    
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date', '-time']

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'question']

    def __str__(self):
        return self.question

class WebsiteContent(models.Model):
    hero_heading = models.CharField(max_length=255, default="One Place for All Government & Digital Services")
    hero_subtitle = models.TextField(default="Your trusted CSC Centre for all online services.")
    about_us_intro = models.TextField(blank=True)
    about_us_mission = models.TextField(blank=True)
    about_us_vision = models.TextField(blank=True)
    years_of_experience = models.IntegerField(default=1)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_address = models.TextField(blank=True)
    business_hours = models.TextField(blank=True)
    whatsapp_number = models.CharField(max_length=20, blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.pk and WebsiteContent.objects.exists():
            return
        super().save(*args, **kwargs)
        
    def __str__(self):
        return "Website Global Content"
