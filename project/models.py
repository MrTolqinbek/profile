from django.db import models
import uuid
from autoslug import AutoSlugField
import re
from user.models import Profile


def fro(instance):
    return instance.title


def slu(value):
    return re.sub('\s+', '-', value)


def upload_(instance, filename):
    return "projects/"+instance.title+"."+filename.split(sep=".")[-1]


class Project(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField("Tag", blank=True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL,null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField(
        null=True, blank=True, default="/projects/default.jpg", upload_to=upload_)
    created = models.DateTimeField(auto_now_add=True)
    vote_total = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    slug = AutoSlugField(populate_from=fro,
                         slugify=slu, unique=True)

    def __str__(self):
        return self.slug


class Review(models.Model):
    VOTE_TYPE = (("up", "UP vote"), ("down", "DOWN vote"),)
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=255, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
