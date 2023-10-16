from django.contrib import admin

from .models import ToDo, Task

admin.site.register(ToDo)
admin.site.register(Task)