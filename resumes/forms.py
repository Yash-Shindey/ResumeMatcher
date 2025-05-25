from django import forms
from .models import Resume

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control'})
        }
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if not file.name.endswith(('.pdf', '.doc', '.docx')):
                raise forms.ValidationError('Only PDF and Word documents are allowed.')
            if file.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError('File size must be under 5MB.')
        return file

class ResumeReviewForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['skills', 'experience', 'education']
        widgets = {
            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Comma-separated skills'}),
            'experience': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'education': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        } 