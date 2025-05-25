from django.db import models
from resumes.models import Resume
from jobs.models import Job

class JobMatch(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    match_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Detailed matching scores
    skills_match_score = models.FloatField()
    experience_match_score = models.FloatField()
    education_match_score = models.FloatField()
    
    # Matching details
    matching_skills = models.TextField(blank=True)
    matching_experience = models.TextField(blank=True)
    matching_education = models.TextField(blank=True)
    
    def __str__(self):
        return f"Match: {self.resume.user.username} - {self.job.title} ({self.match_score}%)"
    
    class Meta:
        ordering = ['-match_score']
        unique_together = ['resume', 'job']
