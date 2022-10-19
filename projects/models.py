from django.db import models
from django_quill.fields import QuillField




PROJECT_STATUS_CHOICE = (
            ("New", "New"),
            ("Backlog", "Backlog"),
            ("Blocked", "Blocked"),
            ("In Progress", "In Progress"),
            ("Test/Review", "Test/Review"),
            ("Closed", "Closed"),
)

QUOTE_APPROVAL_STATUS = (
            ("REJECTED", "REJECTED"),
            ("DRAFT", "DRAFT"),
            ("APPROVED", "APPROVED"),
)

RATING_SCORE = (
            (1, "1 Star"),
            (2, "2 Star"),
            (3, "3 Star"),
            (4, "4 Star"),
            (5, "5 Star"),
)

RFC_APPROVAL = (
            (1, "Waiting"),
            (2, "Approved"),
            (3, "Rejected"),
            (4, "Cancel"),
)

RFC_IMPACT = (
            (3, "High"),
            (2, "Medium"),
            (1, "Low"),
)

RFC_PRIORITY = (
            (4, "Critical"),
            (3, "High"),
            (2, "Medium"),
            (1, "Low"),
)

RFC_RISK = (
            (5, "Very High"),
            (4, "High"),
            (3, "Moderate"),
            (2, "Low"),
            (1, "None"),
)

RFC_STATUS = (
            (1, "Draft"),
            (2, "Waiting for approval"),
            (3, "Approved"),
            (4, "Started"),
            (5, "Finished"),
            (6, "Rejected"),
)

RFC_TYPE = (
            (4, "Emergency"),
            (3, "High"),
            (2, "Medium"),
            (1, "Low"),
)

WANT_CHOICE = (
    ("0", "Do not want to do"),
            ("1", "Want to do"),
)
SKILL_CHOICE = (
    ("0", "Can not do"),
            ("1", "Willing to learn"),
            ("2", "Knows a little"),
            ("3", "Knows a lot"),
            ("4", "Proficient"),
)

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
    ProjectClientBudget = models.CharField()
    projectEastemateCost  = models.CharField() 

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
    pass
    # Only Assain on task user can submitted their task in tasksubmission
    # task_name =
    TodayWorkStarttime = models.DateTimeField()
    TodayWorkEndTime = models.DateTimeField()
    TotalWorkingTimeToday = TodayWorkEndTime - TodayWorkStarttime
    TotalDataEntryToday = models.CharField()
    DataEntryPerHour = TotalDataEntryToday / TotalWorkingTimeToday
    ProjectFile = models.FileField(upload_to=None, max_length=254)
    ProjectSubmissionDescription = QuillField()



class WorkerProjectRecord(models.Model):
    pass
    #ToDo: Total Project Done by user
    #ToDo: Total Project Record by user
    #ToDo: Total Entry by User per week , month, year
    #ToDo: Total Project
    #ToDo: Total Project Done




# Hey,
# Arif Bhy In above I have added many choices that can assain as project pirity , risk and many more you can add this If you thinik this is good !
