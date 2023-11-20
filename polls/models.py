from django.db import models
from django.contrib.auth.models import User
class ToDoList(models.Model):
    name = models.CharField(max_length=60, default="Unnamed")

    def __str__(self):
        return self.name
class Task(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=256)
    complete = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now=True)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    def __str__(self):

        return self.title

    class Meta:
        ordering = ['complete']