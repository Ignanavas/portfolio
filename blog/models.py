from email.policy import default
from turtle import title
from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(default = " ")
    create_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title