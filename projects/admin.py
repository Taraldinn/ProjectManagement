from django.contrib import admin

from projects.models import Categories, Project, Task, TaskSubmission

admin.site.register(Categories)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TaskSubmission)
