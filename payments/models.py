from django.db import models
from accounts.models import User
from projects.models import Project

# Payment model
class PaymentProjectBased(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='payments', blank=False, null=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leader_payments', blank=False, null=False)
    receivers = models.ManyToManyField(User, related_name='worker_payments', blank=False)
    amount = models.FloatField(default=0, blank=False, null=False)
    per_entry = models.FloatField(default=0, blank=True, null=True)
    salary = models.FloatField(default=0, blank=True, null=True)
    is_received = models.BooleanField(default=False)
    is_accept = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Payment to {self.project}"
    
    class Meta:
        verbose_name_plural = 'Payments Employe'
