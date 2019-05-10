from django.db import models



class Subscribers(models.Model):
    """A subscriber model."""
    email = models.CharField(blank=False, null=False, max_length=100, help_text='Email Address')
    full_name = models.CharField(blank=True, null=True, max_length=80, help_text="Full Name")

    def __str__(self):
        """Str repr of this object"""
        return self.full_name
        
    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"