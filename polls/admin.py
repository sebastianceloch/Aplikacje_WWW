from django.contrib import admin

from .models import Person,Job
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ['date_added']
    list_display = ['name', 'surrname', 'sex_type', 'date_added', 'view_job']
    list_filter = ('job', 'date_added')
    @admin.display(empty_value="Stanowisko (Brak)")
    def view_job(self, obj):
        return f'{obj.job.name} ({obj.job.id})'
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_filter = ('name',)