from django.db import models
from django.utils import timezone

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    
    # Job details
    job_type = models.CharField(max_length=50, choices=[
        ('FULL_TIME', 'Full Time'),
        ('PART_TIME', 'Part Time'),
        ('CONTRACT', 'Contract'),
        ('INTERNSHIP', 'Internship'),
    ])
    salary_range = models.CharField(max_length=100, blank=True)
    
    # Required skills and qualifications
    required_skills = models.TextField()
    required_experience = models.TextField()
    required_education = models.TextField()
    
    # Analysis fields
    skills_keywords = models.TextField(blank=True)
    experience_keywords = models.TextField(blank=True)
    education_keywords = models.TextField(blank=True)
    
    # Richer job and company details
    notice_period = models.CharField(max_length=50, blank=True)
    founders = models.CharField(max_length=255, blank=True)
    company_size = models.CharField(max_length=100, blank=True)
    company_website = models.URLField(blank=True)
    job_summary = models.TextField(blank=True)
    benefits = models.TextField(blank=True)
    work_mode = models.CharField(max_length=20, choices=[('REMOTE', 'Remote'), ('HYBRID', 'Hybrid'), ('ONSITE', 'Onsite')], blank=True)
    industry = models.CharField(max_length=100, blank=True)
    linkedin_url = models.URLField(blank=True)
    indeed_url = models.URLField(blank=True)
    glassdoor_url = models.URLField(blank=True)
    company_description = models.TextField(blank=True)
    job_highlights = models.TextField(blank=True)
    application_deadline = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} at {self.company}"
    
    class Meta:
        ordering = ['-posted_at']
