from django.db import models

class Event(models.Model):
    """Model for storing event information"""
    
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('past', 'Past'),
    ]
    
    name = models.CharField(max_length=200, help_text="Name of the event")
    description = models.TextField(help_text="Event description")
    timing = models.CharField(max_length=100, help_text="Event timing (e.g., 2:00 PM - 5:00 PM)")
    location = models.CharField(max_length=200, help_text="Event location")
    additional_info = models.TextField(
        blank=True,
        null=True,
        help_text="Additional information about the event (e.g., number of spots)"
    )
    date = models.DateField(help_text="Event date")
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='upcoming',
        help_text="Event status - automatically determines if shown in upcoming or past events"
    )
    image = models.ImageField(
        upload_to='events/',
        help_text="Event image"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
    
    def __str__(self):
        return f"{self.name} - {self.date}"
    
    @property
    def is_upcoming(self):
        """Check if event is upcoming"""
        return self.status == 'upcoming'
    
    @property
    def is_past(self):
        """Check if event is past"""
        return self.status == 'past'
