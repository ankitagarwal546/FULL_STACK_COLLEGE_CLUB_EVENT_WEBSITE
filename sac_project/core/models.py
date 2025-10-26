from django.db import models

class ContactMessage(models.Model):
    """Model for storing contact form submissions"""
    
    name = models.CharField(max_length=200, help_text="Name of the person")
    email = models.EmailField(help_text="Email address")
    subject = models.CharField(max_length=300, help_text="Message subject")
    message = models.TextField(help_text="Message content")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, help_text="Mark as read")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
