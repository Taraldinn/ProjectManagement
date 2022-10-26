from django import forms
from projects.models import Categories, Project, Task, TaskSubmission
from django.contrib.auth import get_user_model

User = get_user_model()

class ProjectModelForm(forms.ModelForm):
    worker = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(user_type='worker'),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Project
        fields = [
            'name',
            'category',
            'worker',
            'status',
            'work_start_date',
            'work_end_date',
            'deadline',
            'project_client_budget',
            'project_eastemate_cost',
            'sort_description',
            'description',
            'complete_per',
            'file',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project name *'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'work_start_date': forms.DateInput(attrs={'class': 'form-select datepicker-here', 'data-language':'en'}),
            'work_end_date': forms.DateInput(attrs={'class': 'form-select datepicker-here', 'data-language':'en'}),
            'deadline': forms.DateInput(attrs={'class': 'form-select datepicker-here', 'data-language':'en'}),
            'project_client_budget': forms.NumberInput(attrs={'class': 'form-control'}),
            'project_eastemate_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'sort_description': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleFormControlTextarea4', 'rows':'3'}),
            
        }