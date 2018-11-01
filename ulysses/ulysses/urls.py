"""ulysses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django
from django.contrib import admin
from django.urls import path
# Users
from users import views as users_views
# Posts
from posts import views as posts_views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls, name="admin"),
    # Post
    path("posts/", posts_views.holapost, name=""),
    # User
    path("index/", users_views.index, name="index"),
    path("about/", users_views.about, name="about"),
    path("signin/", users_views.signins, name="signin"),
    path("skills/", users_views.skills, name="skills")
]
