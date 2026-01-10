from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=200)
    isCompleted = models.BooleanField(default=False)
    description = models.TextField(max_length=1000,default = "", blank=True)

    def __str__(self):
        return f"{self.task}"