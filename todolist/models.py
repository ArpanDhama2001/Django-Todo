from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=200)
    isCompleted = models.BooleanField(default=False)
    description = models.TextField(max_length=1000,default = "", blank=True)

    def __str__(self):
        return f"{self.task}"