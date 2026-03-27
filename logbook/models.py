from django.db import models

# Create your models here.
class LearningEvent(models.Model):
    topic = models.CharField(max_length=255)
    confidence = models.IntegerField()
    feeling = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    duration = models.DurationField(blank=True, null=True)