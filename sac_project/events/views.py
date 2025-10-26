from django.shortcuts import render
from .models import Event

def events_list(request):
    """View for displaying upcoming and past events"""
    upcoming_events = Event.objects.filter(status='upcoming').order_by('date')
    past_events = Event.objects.filter(status='past').order_by('-date')
    
    context = {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    }
    return render(request, 'events/events.html', context)
