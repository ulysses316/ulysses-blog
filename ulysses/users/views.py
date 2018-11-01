# Django
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "templatesbase/index.html")

def about(request):
    return render(request, "templatesbase/about.html")

def signins(request):
    return render(request, "templatesbase/signin.html")

def skills(request):
    return render(request, "templatesbase/skills.html")
