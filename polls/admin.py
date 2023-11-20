from django.contrib import admin
from polls.models import ToDoList, Task

admin.site.register(ToDoList)
admin.site.register(Task)
