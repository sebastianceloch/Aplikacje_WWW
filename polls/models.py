from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    home_address = models.CharField(max_length=256, blank=False)
    phone_number = models.CharField(max_length=9, blank=False)
    avatar = models.ImageField(upload_to='media', null=True, blank=True)
    def __str__(self):
        return f"{self.username} - {self.home_address}"

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
    description = models.CharField(max_length=256, blank=True, null=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now=True)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):

        return self.title

    class Meta:
        ordering = ['complete']