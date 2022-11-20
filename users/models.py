from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=50)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    bio = models.TextField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=100)
    short_intro = models.TextField(max_length=100, blank=True, null=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_stackoverflow = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    created = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return self.username


class Skills(models.Model):
    owner = models.ForeignKey(Profiles, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(Profiles, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profiles, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']

