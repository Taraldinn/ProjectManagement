from email.policy import default
from django.db import models
from django_quill.fields import QuillField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

    
#ToDo: Total Project Done by user
#ToDo: Total Project Record by user
#ToDo: Total Entry by User per week , month, year
#ToDo: Total Project
#ToDo: Total Project Done

# a user can submit single time for a project -> task submission editable valided for the 24 hours




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

STATUS = (
            ('1', 'Stuck'),
            ('2', 'Working'),
            ('3', 'Done'),
)

DUE = (
            ('1', 'On Due'),
            ('2', 'Overdue'),
            ('3', 'Done'),
)


class Project(models.Model):
    name = models.CharField(max_length=255)
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    worker = models.ManyToManyField(User)
    status = models.CharField(max_length=7, choices=STATUS, default=1)
    complete_per = models.FloatField(max_length=2, validators = [MinValueValidator(0), MaxValueValidator(100)])
    description = QuillField()
    deadline = models.DateField()
    project_client_budget = models.FloatField(default=0)
    project_eastemate_cost = models.FloatField(default=0)
    work_start_date = models.DateField()
    work_end_date = models.DateField()
    is_active = models.BooleanField(default=False)
    file = models.FileField(upload_to='project_file')
    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return (self.name)

    def total_project_done_by_user(self):
        pass


class Task(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    worker = models.ManyToManyField(User)
    status = models.CharField(max_length=7, choices=STATUS, default=1)
    due = models.CharField(max_length=7, choices=DUE, default=1)
    description = QuillField()
    deadline = models.DateField()
    is_active = models.BooleanField(default=False)
    file = models.FileField(upload_to='project_task')

    class Meta:
        ordering = ['project', 'name']

    def __str__(self):
        return(self.name)


class TaskSubmission(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name= 'task_submissions')
    today_start_work = models.DateTimeField()
    today_end_work = models.DateTimeField()
    total_data_entry_today = models.CharField(max_length=254)
    file = models.FileField(upload_to='project_task_submission', max_length=254)
    description = QuillField()

    def __str__(self):
        return f"task submission of => {self.project.name}"

    def total_hours_today(self):
        pass

    def data_entry_per_hour(self):
        pass


# Hey,
# Arif Bhy In above I have added many choices that can assain as project pirity , risk and many more you can add this If you thinik this is good !
