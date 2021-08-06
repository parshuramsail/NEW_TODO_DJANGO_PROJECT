from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
