from django.contrib import admin

from projects.models import Project, Task, TaskSubmission

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TaskSubmission)
