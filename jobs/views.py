from django.shortcuts import render, get_object_or_404
from .models import Job
from datetime import date


def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html', {'jobs': jobs, 'year': date.today().year})


def show(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/show.html', {'job': job})
