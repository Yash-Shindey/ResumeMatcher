from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title', 'company', 'location', 'description', 'requirements',
            'job_type', 'salary_range', 'required_skills', 'required_experience',
            'required_education'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
            'salary_range': forms.TextInput(attrs={'class': 'form-control'}),
            'required_skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'required_experience': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'required_education': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        } 