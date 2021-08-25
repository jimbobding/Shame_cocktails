from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Drinks(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    method = models.TextField()
    glassware = models.CharField(max_length=100)
    garnish = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

