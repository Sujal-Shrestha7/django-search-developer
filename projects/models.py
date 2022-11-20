import uuid

from django.db import models
from users.models import Profiles

# Create your models here.


def reviewers(args):
    pass


class Projects(models.Model):
    owner = models.ForeignKey(Profiles, blank=True, null=True, on_delete=models.SET_NULL )
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    demo_link = models.CharField(max_length=200, null=True, blank=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    vote_total = models.IntegerField(null=True, blank=True, default=0)
    vote_ratio = models.IntegerField(null=True, blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    @property
    def reviewers(self):
        queryset = self.reviews_set.all.values_list('owner__id', flat=True)
        return queryset

    @property
    def get_vote_count(self):
        review = self.reviews_set.all()
        upvote = review.filter(value='Up').count()
        total_vote = review.count()

        ratio = (upvote / total_vote) * 100
        self.vote_total = total_vote
        self.vote_ratio = ratio
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-vote_ratio', '-vote_total', 'title']


class Reviews(models.Model):
    Vote_Type = (
        ('Up', 'Up Vote'),
        ('Down', 'Down Vote'),
    )
    owner = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True)
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    value = models.CharField(max_length=200, choices=Vote_Type, verbose_name= 'vote Up/Down')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together = [['owner', 'projects']]

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name



