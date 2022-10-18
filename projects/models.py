from django.db import models
from django_quill.fields import QuillField

# Create your models here.
status = (
    ('1', 'Stuck'),
            ('2', 'Working'),
            ('3', 'Done'),
)

due = (
    ('1', 'On Due'),
            ('2', 'Overdue'),
            ('3', 'Done'),
)


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    # Assain Worker And Leader To This Project
    # project_lead = models.ForeignKey(User, on_delete=models.CASCADE)
    # assign = models.ManyToManyField(User, related_name="project_assign")
    # efforts = models.DurationField()
    status = models.CharField(max_length=7, choices=status, default=1)
    complete_per = models.FloatField(max_length=2, validators = [MinValueValidator(0), MaxValueValidator(100)])
    description = QuillField()
    deadline = models.DateField()

    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return (self.name)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="task_project_assign")
    # Assain Only worker to the task . and worker should be only on for only one task
    # assign = models.ManyToManyField(User, related_name="task_assign")
    task_name = models.CharField(max_length=80)
    project_file = models.FileField(upload_to=None, max_length=254, **options)
    status = models.CharField(max_length=7, choices=status, default=1)
    due = models.CharField(max_length=7, choices=due, default=1)
    description = QuillField()
    deadline = models.DateField()

    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return(self.task_name)


class TaskSubmission(models.Model):
    # task_name =
    TodayWorkStarttime = models.DateTimeField()
    TodayWorkEndTime = models.DateTimeField()
    TotalWorkingTimeToday = TodayWorkEndTime - TodayWorkStarttime
    TotalDataEntryToday = models.CharField()
    DataEntryPerHour = TotalDataEntryToday / TotalWorkingTimeToday
    ProjectFile = models.FileField(upload_to=None, max_length=254, **options)

