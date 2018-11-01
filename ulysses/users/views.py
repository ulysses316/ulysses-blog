# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    return render(request, "templatesbase/index.html")

def about(request):
    return render(request, "templatesbase/about.html")

def skills(request):
    return render(request, "templatesbase/skills.html")

def signins(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "templatesbase/signin.html", {"error": "Invalid Username or password"})
    return render(request, "templatesbase/signin.html")
