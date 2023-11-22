from django.contrib import admin
from polls.models import ToDoList, Task, Category, UserProfile

admin.site.register(ToDoList)
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(UserProfile)