from django import forms
from django.contrib.auth import get_user_model

from payments.models import PaymentProjectBased
User = get_user_model()


class PaymentProjectBasedForm(forms.ModelForm):
    receivers = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(user_type='worker'),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = PaymentProjectBased
        fields = [
            'amount',
            'receivers',
        ]
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}), 
        }

