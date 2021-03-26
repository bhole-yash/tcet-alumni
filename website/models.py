from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Notification(models.Model):
    NEWS_TYPE = (
        ("Infomative", "Informative"),
        ("Events", "Events"),
        ("Urgent", "Urgent"),
    )
    Title = models.CharField(max_length=100)
    Type = models.CharField(max_length=100, choices=NEWS_TYPE)
    description = models.TextField(max_length=2500)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Title


