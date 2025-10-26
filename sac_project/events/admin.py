from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Admin interface for Event model"""
    
    list_display = ['name', 'date', 'status', 'location', 'timing', 'created_at']
    list_filter = ['status', 'date', 'created_at']
    search_fields = ['name', 'description', 'location']
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'image')
        }),
        ('Event Details', {
            'fields': ('date', 'timing', 'location', 'additional_info')
        }),
        ('Status', {
            'fields': ('status',),
            'description': 'Mark as "Past" to move the event from upcoming to past events section.'
        }),
    )
    
    actions = ['mark_as_past', 'mark_as_upcoming']
    
    def mark_as_past(self, request, queryset):
        """Action to mark selected events as past"""
        updated = queryset.update(status='past')
        self.message_user(request, f'{updated} event(s) marked as past.')
    mark_as_past.short_description = 'Mark selected events as Past'
    
    def mark_as_upcoming(self, request, queryset):
        """Action to mark selected events as upcoming"""
        updated = queryset.update(status='upcoming')
        self.message_user(request, f'{updated} event(s) marked as upcoming.')
    mark_as_upcoming.short_description = 'Mark selected events as Upcoming'
