from django.db import models

class Club(models.Model):
    """Model for storing club information"""
    
    REGISTRATION_STATUS_CHOICES = [
        ('open', 'Registration Open'),
        ('closed', 'Registration Closed'),
    ]
    
    name = models.CharField(max_length=200, help_text="Name of the club")
    description = models.TextField(help_text="Club description")
    registration_status = models.CharField(
        max_length=10,
        choices=REGISTRATION_STATUS_CHOICES,
        default='closed',
        help_text="Current registration status"
    )
    spots = models.IntegerField(default=0, help_text="Number of available spots")
    image = models.ImageField(
        upload_to='clubs/',
        help_text="Club image"
    )
    google_form_link = models.URLField(
        blank=True,
        null=True,
        help_text="Google Form link for registration (Apply Now button will only appear if this is filled)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'
    
    def __str__(self):
        return self.name
    
    @property
    def has_registration_link(self):
        """Check if the club has a registration link"""
        return bool(self.google_form_link)
