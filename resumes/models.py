from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(default=timezone.now)
    
    # Extracted information
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    skills = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    
    # Analysis results
    skills_score = models.FloatField(default=0)
    experience_score = models.FloatField(default=0)
    education_score = models.FloatField(default=0)
    overall_score = models.FloatField(default=0)
    
    def __str__(self):
        return f"{self.user.username}'s Resume - {self.uploaded_at.strftime('%Y-%m-%d')}"
    
    class Meta:
        ordering = ['-uploaded_at']
