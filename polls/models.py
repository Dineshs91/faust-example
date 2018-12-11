from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Poll(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    question = models.TextField()


class UserVote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.BooleanField(default=False)
