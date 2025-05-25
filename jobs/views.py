from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job
from .forms import JobForm
from matching.models import JobMatch

@login_required
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/list.html', {'jobs': jobs})

@login_required
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    matches = JobMatch.objects.filter(job=job).order_by('-match_score')
    return render(request, 'jobs/detail.html', {
        'job': job,
        'matches': matches
    })

@login_required
def create_job(request):
    if not request.user.userprofile.is_admin:
        messages.error(request, 'Only admins can create jobs.')
        return redirect('job_list')
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save()
            messages.success(request, 'Job created successfully!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm()
    return render(request, 'jobs/create.html', {'form': form})

@login_required
def edit_job(request, pk):
    if not request.user.userprofile.is_admin:
        messages.error(request, 'Only admins can edit jobs.')
        return redirect('job_list')
    
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/edit.html', {'form': form, 'job': job})

@login_required
def delete_job(request, pk):
    if not request.user.userprofile.is_admin:
        messages.error(request, 'Only admins can delete jobs.')
        return redirect('job_list')
    
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')
        return redirect('job_list')
    return render(request, 'jobs/delete.html', {'job': job})
