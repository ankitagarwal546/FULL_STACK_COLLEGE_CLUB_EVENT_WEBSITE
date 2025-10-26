from django.db import models

class GalleryPhoto(models.Model):
    """Model for storing gallery photos"""
    
    SECTION_CHOICES = [
        ('workshops', 'Workshops'),
        ('events', 'Events'),
        ('projects', 'Projects'),
        ('social', 'Social'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200, help_text="Photo title")
    image = models.ImageField(upload_to='gallery/', help_text="Upload photo")
    section = models.CharField(
        max_length=20,
        choices=SECTION_CHOICES,
        help_text="Select the section where this photo should appear"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Gallery Photo'
        verbose_name_plural = 'Gallery Photos'
    
    def __str__(self):
        return f"{self.title} - {self.get_section_display()}"
