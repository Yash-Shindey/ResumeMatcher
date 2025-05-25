from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import JobMatch
from resumes.models import Resume
from jobs.models import Job

# Create your views here.

@login_required
def match_list(request):
    try:
        matches = JobMatch.objects.filter(resume__user=request.user).order_by('-match_score')
        return render(request, 'matching/list.html', {'matches': matches})
    except Exception as e:
        messages.error(request, 'An error occurred while fetching matches.')
        return redirect('dashboard')

@login_required
def match_detail(request, pk):
    try:
        match = get_object_or_404(JobMatch, pk=pk)
        if match.resume.user != request.user:
            messages.error(request, 'You do not have permission to view this match.')
            return redirect('match_list')
        return render(request, 'matching/detail.html', {'match': match})
    except Exception as e:
        messages.error(request, 'An error occurred while fetching match details.')
        return redirect('match_list')

@login_required
def generate_matches(request, resume_id):
    try:
        resume = get_object_or_404(Resume, pk=resume_id, user=request.user)
        from resumes.views import create_job_matches
        create_job_matches(resume)
        messages.success(request, 'Job matches generated successfully!')
        return redirect('resume_detail', pk=resume_id)
    except Exception as e:
        messages.error(request, 'An error occurred while generating matches.')
        return redirect('resume_detail', pk=resume_id)

@login_required
def admin_dashboard(request):
    if not request.user.userprofile.is_admin:
        return redirect('dashboard')
    
    # Get statistics
    total_resumes = Resume.objects.count()
    total_jobs = Job.objects.count()
    total_matches = JobMatch.objects.count()
    
    # Get top matches
    top_matches = JobMatch.objects.all().order_by('-match_score')[:10]
    
    # Get job distribution
    job_types = Job.objects.values_list('job_type', flat=True).distinct()
    job_distribution = {
        job_type: Job.objects.filter(job_type=job_type).count()
        for job_type in job_types
    }
    
    context = {
        'total_resumes': total_resumes,
        'total_jobs': total_jobs,
        'total_matches': total_matches,
        'top_matches': top_matches,
        'job_distribution': job_distribution,
    }
    
    return render(request, 'matching/admin_dashboard.html', context)
