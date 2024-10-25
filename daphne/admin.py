from django.contrib import admin
from .models import Job, Daphne, Shift

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    ordering = ['title']

@admin.register(Daphne)
class DaphneAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'get_jobs')
    search_fields = ('user__username', 'phone')
    list_filter = ('user',)
    ordering = ['user']
    
    def get_jobs(self, obj):
        return ", ".join(job.title for job in obj.jobs.all())
    get_jobs.short_description = 'Job Titles'

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('daphne', 'date', 'start_time', 'end_time', 'get_duration')
    search_fields = ('daphne__user__username',)
    list_filter = ('date', 'daphne')
    ordering = ['date', 'start_time']

    def get_duration(self, obj):
        return str(obj.duration())
    get_duration.short_description = 'Duration'
