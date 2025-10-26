from django.shortcuts import render
from .models import Club

def clubs_list(request):
    """View for displaying all clubs"""
    clubs = Club.objects.all()
    context = {
        'clubs': clubs,
    }
    return render(request, 'clubs/about.html', context)
