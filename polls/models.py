from django.db import models

# Create your models here.
class ToDo(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE)
    def __str__(self):
        return self.name