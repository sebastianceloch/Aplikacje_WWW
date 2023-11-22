from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField(max_length=100, default="Unnamed")

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class ToDoList(models.Model):
    name = models.CharField(max_length=60, default="Unnamed")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
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

class UserProfile(models.Model):
    home_address = models.CharField(max_length=256, null=True)
    phone_number = models.CharField(max_length=9, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.home_address}"
