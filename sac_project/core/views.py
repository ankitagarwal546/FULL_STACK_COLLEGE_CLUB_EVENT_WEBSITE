from django.shortcuts import render, redirect
from django.contrib import messages
from events.models import Event
from .models import ContactMessage

def home(request):
    """View for home page"""
    # Get first 3 upcoming events for homepage
    upcoming_events = Event.objects.filter(status='upcoming').order_by('date')[:3]
    context = {
        'upcoming_events': upcoming_events,
    }
    return render(request, 'core/index.html', context)

def contact(request):
    """View for contact page"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Create contact message
        contact_msg = ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        print(f"✓ Contact message saved! ID: {contact_msg.id}, Name: {name}, Email: {email}")
        
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return redirect('core:contact')
    
    return render(request, 'core/contact.html')

def members(request):
    """View for members page"""
    return render(request, 'core/members.html')
