from django.contrib import admin
from .models import Club

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    """Admin interface for Club model"""
    
    list_display = ['name', 'registration_status', 'spots', 'has_registration_link', 'created_at']
    list_filter = ['registration_status', 'created_at']
    search_fields = ['name', 'description']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'image')
        }),
        ('Registration Details', {
            'fields': ('registration_status', 'spots', 'google_form_link'),
            'description': 'The "Apply Now" button will only appear on the frontend if a Google Form link is provided.'
        }),
    )
    
    readonly_fields = []
    
    def has_registration_link(self, obj):
        """Display if the club has a registration link"""
        return obj.has_registration_link
    has_registration_link.short_description = 'Has Form Link'
    has_registration_link.boolean = True
