from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import subjectsByClass


def index(request):
    return render(request, 'samplesite/index.html')

def marks(request):
    return render(request, 'samplesite/marks.html')

def subjects(request):
    return render(request, 'samplesite/subjects.html')

def notebook(request):
    return render(request, 'samplesite/notebook.html')

def login(request):
    return render(request, 'samplesite/login.html')