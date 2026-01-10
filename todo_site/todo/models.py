from django.db import models
"""Edit todo/models.py to define the Todo model.
 The model represents each to-do item with a title, description, and creation time."""
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 100)
    details = models.TextField()
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title