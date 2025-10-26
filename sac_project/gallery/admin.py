from django.contrib import admin
from .models import GalleryPhoto

@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    """Admin interface for GalleryPhoto model"""
    
    list_display = ['title', 'section', 'created_at', 'image_preview']
    list_filter = ['section', 'created_at']
    search_fields = ['title']
    
    fieldsets = (
        ('Photo Information', {
            'fields': ('title', 'section', 'image')
        }),
    )
    
    def image_preview(self, obj):
        """Display a preview of the image in the admin list"""
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 50px; max-width: 50px; object-fit: cover;" />'
        return '-'
    image_preview.short_description = 'Preview'
    image_preview.allow_tags = True
