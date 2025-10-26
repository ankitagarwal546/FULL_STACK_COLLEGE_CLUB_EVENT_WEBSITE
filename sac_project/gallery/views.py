from django.shortcuts import render
from .models import GalleryPhoto

def gallery_list(request):
    """View for displaying gallery photos"""
    # Get filter parameter from URL
    filter_section = request.GET.get('filter', 'all')
    
    # Filter photos based on section
    if filter_section == 'all' or not filter_section:
        photos = GalleryPhoto.objects.all()
    else:
        photos = GalleryPhoto.objects.filter(section=filter_section)
    
    context = {
        'photos': photos,
        'current_filter': filter_section,
    }
    return render(request, 'gallery/gallery.html', context)
