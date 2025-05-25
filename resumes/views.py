from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Resume
from .forms import ResumeUploadForm, ResumeReviewForm
from matching.models import JobMatch
import spacy
import PyPDF2
import docx
import re
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST
from django.core.files.base import ContentFile

def extract_text_from_pdf(file):
    try:
        text = ""
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        raise ValidationError('Error reading PDF file')

def extract_text_from_docx(file):
    try:
        doc = docx.Document(file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        raise ValidationError('Error reading DOCX file')

def extract_skills(text):
    try:
        # Load spaCy model
        nlp = spacy.load("en_core_web_sm")
        
        # Comprehensive list of technical skills
        technical_skills = {
            'programming_languages': [
                'python', 'java', 'javascript', 'typescript', 'c#', 'c++', 'ruby', 'php',
                'swift', 'kotlin', 'go', 'rust', 'scala', 'perl', 'r', 'matlab'
            ],
            'web_technologies': [
                'html', 'css', 'react', 'angular', 'vue', 'node.js', 'express', 'django',
                'flask', 'spring', 'laravel', 'asp.net', 'jquery', 'bootstrap', 'sass',
                'webpack', 'babel', 'redux', 'graphql', 'rest', 'soap'
            ],
            'databases': [
                'sql', 'mysql', 'postgresql', 'oracle', 'mongodb', 'redis', 'cassandra',
                'elasticsearch', 'dynamodb', 'firebase', 'neo4j'
            ],
            'cloud_platforms': [
                'aws', 'azure', 'gcp', 'heroku', 'digitalocean', 'linode', 'vultr'
            ],
            'devops_tools': [
                'docker', 'kubernetes', 'jenkins', 'gitlab', 'github actions', 'terraform',
                'ansible', 'puppet', 'chef', 'prometheus', 'grafana', 'elk stack'
            ],
            'ai_ml': [
                'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'keras',
                'scikit-learn', 'numpy', 'pandas', 'opencv', 'nltk', 'spacy'
            ],
            'mobile_dev': [
                'android', 'ios', 'react native', 'flutter', 'xamarin', 'ionic'
            ],
            'design_tools': [
                'figma', 'adobe xd', 'sketch', 'photoshop', 'illustrator', 'indesign'
            ],
            'testing_tools': [
                'selenium', 'jest', 'pytest', 'junit', 'cypress', 'postman', 'jmeter'
            ],
            'other_skills': [
                'git', 'agile', 'scrum', 'jira', 'confluence', 'linux', 'networking',
                'security', 'blockchain', 'solidity', 'web3', 'ethereum', 'smart contracts'
            ]
        }
        
        # Combine all skills into a single list
        all_skills = []
        for category in technical_skills.values():
            all_skills.extend(category)
        
        # Extract skills using spaCy
        doc = nlp(text.lower())
        skills = []
        
        # Check for technical skills
        for skill in all_skills:
            if skill in text.lower():
                skills.append(skill)
        
        # Extract named entities that might be skills
        for ent in doc.ents:
            if ent.label_ in ["ORG", "PRODUCT"]:
                skills.append(ent.text.lower())
        
        # Extract education
        education = extract_education(text)
        
        # Extract experience
        experience = extract_experience(text)
        
        return {
            'skills': list(set(skills)),
            'education': education,
            'experience': experience
        }
    except Exception as e:
        return {
            'skills': [],
            'education': '',
            'experience': ''
        }

def extract_education(text):
    try:
        # Common education patterns
        education_patterns = [
            r'(?i)(bachelor|master|phd|doctorate|b\.s\.|m\.s\.|b\.a\.|m\.a\.).*?(in|of|,).*?(\w+)',
            r'(?i)(bachelor|master|phd|doctorate|b\.s\.|m\.s\.|b\.a\.|m\.a\.).*?(\w+)',
            r'(?i)(university|college|institute).*?(degree|bachelor|master|phd)'
        ]
        
        for pattern in education_patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(0)
        
        return ''
    except Exception:
        return ''

def extract_experience(text):
    try:
        # Look for experience patterns
        experience_patterns = [
            r'(\d+)(?:\+)?\s*years?\s*(?:of)?\s*experience',
            r'experience:\s*(\d+)(?:\+)?\s*years?',
            r'(\d+)(?:\+)?\s*years?\s*(?:in)?\s*the\s*field'
        ]
        
        for pattern in experience_patterns:
            match = re.search(pattern, text.lower())
            if match:
                return match.group(0)
        
        return ''
    except Exception:
        return ''

@login_required
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                resume = form.save(commit=False)
                resume.user = request.user
                
                # Extract text based on file type
                file = request.FILES['file']
                if file.name.endswith('.pdf'):
                    text = extract_text_from_pdf(file)
                elif file.name.endswith(('.doc', '.docx')):
                    text = extract_text_from_docx(file)
                else:
                    raise ValidationError('Unsupported file format')
                
                # Extract information
                extracted_info = extract_skills(text)
                resume.skills = ", ".join(extracted_info['skills'])
                resume.education = extracted_info['education']
                resume.experience = extracted_info['experience']
                
                # Save the resume
                resume.save()
                
                # Create job matches
                create_job_matches(resume)
                
                messages.success(request, 'Resume uploaded and analyzed successfully!')
                return redirect('resume_list')
            except ValidationError as e:
                messages.error(request, str(e))
            except Exception as e:
                messages.error(request, 'An error occurred while processing your resume.')
    else:
        form = ResumeUploadForm()
    return render(request, 'resumes/upload.html', {'form': form})

@login_required
def resume_list(request):
    try:
        resumes = Resume.objects.filter(user=request.user)
        return render(request, 'resumes/list.html', {'resumes': resumes})
    except Exception as e:
        messages.error(request, 'An error occurred while fetching your resumes.')
        return redirect('dashboard')

@login_required
def resume_detail(request, pk):
    try:
        resume = get_object_or_404(Resume, pk=pk, user=request.user)
        matches = JobMatch.objects.filter(resume=resume).order_by('-match_score')
        return render(request, 'resumes/detail.html', {
            'resume': resume,
            'matches': matches
        })
    except Exception as e:
        messages.error(request, 'An error occurred while fetching resume details.')
        return redirect('resume_list')

def create_job_matches(resume):
    try:
        from jobs.models import Job
        from matching.models import JobMatch
        
        # Delete existing matches for this resume
        JobMatch.objects.filter(resume=resume).delete()
        
        jobs = Job.objects.all()
        for job in jobs:
            # Calculate match scores
            skills_match = calculate_skills_match(resume.skills, job.required_skills)
            experience_match = calculate_experience_match(resume.experience, job.required_experience)
            education_match = calculate_education_match(resume.education, job.required_education)
            
            # Calculate overall match score (weighted)
            overall_score = (
                skills_match * 0.5 +  # Skills are most important
                experience_match * 0.3 +  # Experience is second
                education_match * 0.2  # Education is least important
            )
            
            # Create job match
            JobMatch.objects.create(
                resume=resume,
                job=job,
                match_score=overall_score,
                skills_match_score=skills_match,
                experience_match_score=experience_match,
                education_match_score=education_match,
                matching_skills=get_matching_skills(resume.skills, job.required_skills),
                matching_experience=get_matching_experience(resume.experience, job.required_experience),
                matching_education=get_matching_education(resume.education, job.required_education)
            )
    except Exception as e:
        raise ValidationError('Error creating job matches')

def calculate_skills_match(resume_skills, job_skills):
    try:
        if not resume_skills or not job_skills:
            return 0
        
        resume_skills_set = set(resume_skills.lower().split(', '))
        job_skills_set = set(job_skills.lower().split(', '))
        
        if not job_skills_set:
            return 0
        
        common_skills = resume_skills_set.intersection(job_skills_set)
        return len(common_skills) / len(job_skills_set) * 100
    except Exception:
        return 0

def calculate_experience_match(resume_exp, job_exp):
    try:
        if not resume_exp or not job_exp:
            return 0
        
        # Extract years from both
        resume_years = extract_years(resume_exp)
        job_years = extract_years(job_exp)
        
        if resume_years >= job_years:
            return 100
        else:
            return (resume_years / job_years) * 100
    except Exception:
        return 0

def calculate_education_match(resume_edu, job_edu):
    try:
        if not resume_edu or not job_edu:
            return 0
        
        # Education levels with their values
        education_levels = {
            'phd': 4,
            'doctorate': 4,
            'master': 3,
            'm.s.': 3,
            'm.a.': 3,
            'bachelor': 2,
            'b.s.': 2,
            'b.a.': 2,
            'associate': 1,
            'high school': 0
        }
        
        resume_level = get_education_level(resume_edu.lower())
        job_level = get_education_level(job_edu.lower())
        
        if resume_level >= job_level:
            return 100
        else:
            return (resume_level / job_level) * 100
    except Exception:
        return 0

def extract_years(text):
    # Extract years of experience from text
    years = 0
    try:
        # Look for patterns like "X years" or "X+ years"
        matches = re.findall(r'(\d+)(?:\+)?\s*years?', text.lower())
        if matches:
            years = max(map(int, matches))
    except Exception:
        pass
    return years

def get_education_level(text):
    education_levels = {
        'phd': 4,
        'doctorate': 4,
        'master': 3,
        'm.s.': 3,
        'm.a.': 3,
        'bachelor': 2,
        'b.s.': 2,
        'b.a.': 2,
        'associate': 1,
        'high school': 0
    }
    
    for level, value in education_levels.items():
        if level in text:
            return value
    return 0

def get_matching_skills(resume_skills, job_skills):
    try:
        if not resume_skills or not job_skills:
            return ""
        
        resume_skills_set = set(resume_skills.lower().split(', '))
        job_skills_set = set(job_skills.lower().split(', '))
        
        common_skills = resume_skills_set.intersection(job_skills_set)
        return ", ".join(common_skills)
    except Exception:
        return ""

def get_matching_experience(resume_exp, job_exp):
    try:
        if not resume_exp or not job_exp:
            return ""
        
        # Return matching experience details
        return f"Resume: {resume_exp}\nRequired: {job_exp}"
    except Exception:
        return ""

def get_matching_education(resume_edu, job_edu):
    try:
        if not resume_edu or not job_edu:
            return ""
        
        # Return matching education details
        return f"Resume: {resume_edu}\nRequired: {job_edu}"
    except Exception:
        return ""

@login_required
@require_POST
def delete_resume(request, pk):
    resume = get_object_or_404(Resume, pk=pk, user=request.user)
    resume.delete()
    messages.success(request, 'Resume deleted successfully!')
    return redirect('resume_list')

@login_required
def review_resume(request):
    data = request.session.get('resume_data')
    if not data:
        messages.error(request, 'No resume data to review. Please upload again.')
        return redirect('upload_resume')
    if request.method == 'POST':
        form = ResumeReviewForm(request.POST)
        if form.is_valid():
            # Save resume with user edits
            resume = Resume(
                user=request.user,
                skills=form.cleaned_data['skills'],
                experience=form.cleaned_data['experience'],
                education=form.cleaned_data['education'],
            )
            # Save file from session
            file_content = data.get('file_content', '').encode('latin1')
            file_name = request.session.get('resume_file_name', 'resume.pdf')
            resume.file.save(file_name, ContentFile(file_content), save=False)
            resume.save()
            create_job_matches(resume)
            messages.success(request, 'Resume uploaded, reviewed, and analyzed successfully!')
            # Clean up session
            for key in ['resume_data', 'resume_file_name', 'resume_file_type']:
                if key in request.session:
                    del request.session[key]
            return redirect('resume_list')
    else:
        form = ResumeReviewForm(initial={
            'skills': data.get('skills', ''),
            'experience': data.get('experience', ''),
            'education': data.get('education', ''),
        })
    return render(request, 'resumes/review.html', {'form': form, 'resume_data': data})
