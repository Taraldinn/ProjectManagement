from django import forms
from django.contrib.auth import get_user_model
from projects.models import Project
from payments.models import PaymentProjectBased
User = get_user_model()

# pay project based form
class PaymentProjectBasedForm(forms.ModelForm):
    receivers = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(user_type='worker'),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = PaymentProjectBased
        fields = [
            'amount',
            'per_entry',
            'receivers',
        ]
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}), 
            'per_entry': forms.NumberInput(attrs={'class': 'form-control'}), 
        }


# pay to direct worker form
class PaymentWorkerForm(forms.ModelForm):
    project = forms.ModelMultipleChoiceField(
        queryset= Project.objects.filter(leader=1),
        widget=forms.Select
    )
    receivers = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(user_type='worker'),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = PaymentProjectBased
        fields = [
            'project',
            'amount',
            'per_entry',
            'receivers',
        ]
        widgets = {
            'project': forms.Select(attrs={'class': 'form-control'}), 
            'amount': forms.NumberInput(attrs={'class': 'form-control'}), 
            'per_entry': forms.NumberInput(attrs={'class': 'form-control'}), 
        }
    
    def __init__(self, user, *args, **kwargs):
        super(PaymentWorkerForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(leader = user)

