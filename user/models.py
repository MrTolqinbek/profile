from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete


def upload_(i, f):
    return "users/"+f


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    shortIntro = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to=upload_, default="/users/default.png")
    github = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    youtube = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.username


class Skill(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

