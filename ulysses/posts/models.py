# Django
from django.db import models
from django.contrib.auth.models import User
# Local
from users.models import Profile
# Create your models here.

class Post(models.Model):
    """
        title
        user (photo)
        user (username)
        created date
        post
    """
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)

    title = models.CharField(max_length=30)
    photo = models.ImageField(upload_to  = "posts/photos")

    created = models.DateTimeField(auto_now_add = True)
    modofied = models.DateTimeField(auto_now = True)
    history = models.TextField()

    def __str__(self):
        """returned a user and the title of post"""
        return "{} by @{}".format(self.title, self.user.username)
