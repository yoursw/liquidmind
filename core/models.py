from django.db import models
from django.conf import settings

class ActivityChoices(models.TextChoices):
    KAYA = 'Kaya', 'Body'
    VEDANA = 'Vedana', 'Feelings'
    CITTA = 'Citta', 'Mind'
    DHAMMA = 'Dhamma', 'Mind Objects'

class Experience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity = models.CharField(max_length=10, choices=ActivityChoices.choices, blank=True)
    duration = models.DurationField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Experience by {self.user.username} on {self.created_at}"