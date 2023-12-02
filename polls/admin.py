from django.contrib import admin
from polls.models import ToDoList, Task, Category
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(ToDoList)
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(User, UserAdmin)

UserAdmin.list_display += ('home_address','phone_number','avatar')
UserAdmin.list_filter += ('home_address','phone_number','avatar')
UserAdmin.fieldsets += (('Extra Fields', {'fields': ('home_address', 'phone_number','avatar')}),)
