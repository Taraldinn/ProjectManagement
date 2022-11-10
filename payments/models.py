from django.db import models
from accounts.models import User
from projects.models import Project
from django.db.models import Q
import datetime

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
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Payment to {self.project}"
    
    class Meta:
        verbose_name_plural = 'Payments Employe'

    def total_entry_amount(self):
        total_entry = 0
        for issues in self.project.issues_set.all():
            total_day_entry = issues.total_data_entry_today
            total_entry += total_day_entry
            return total_entry * 2
        return total_entry * 2

    
    # today earning
    def today_earning(self, user):
        # today earning
        today = datetime.date.today()
        today_earning_obj = PaymentProjectBased.objects.filter(date=today, project__accept_status='accept', receivers=user, is_received=True)
        today_earning = 0
        for today_earn in today_earning_obj:
            today_earning += today_earn.amount
        return today_earning

    # this week earning
    def week_earning(self, user):
        # this week earning
        week_start = datetime.date.today()
        week_start -= datetime.timedelta(days=week_start.weekday())
        week_end = week_start + datetime.timedelta(days=7)
        this_week_earning_obj = PaymentProjectBased.objects.filter(Q(date__gte=week_start, date__lt=week_end) & Q(project__accept_status='accept', receivers=user, is_received=True, is_accept=True))
        week_earning = 0
        for week_earn in this_week_earning_obj:
            week_earning += week_earn.amount
        return week_earning

    # this month earning
    def month_earning(self, user):
        # this month earning
        this_month_earning_obj = PaymentProjectBased.objects.filter(Q(date__gte=datetime.datetime.today().replace(day=1, hour=0, minute=0, second=0, microsecond=0)) & Q(project__accept_status='accept', receivers=user, is_received=True, is_accept=True))
        month_earning = 0
        for month_earn in this_month_earning_obj:
            month_earning += month_earn.amount
        return month_earning

    # this year earning
    def year_earning(self, user):
        # this year earning
        this_year_earning_obj = PaymentProjectBased.objects.filter(Q(date__year=datetime.datetime.now().year) & Q(project__accept_status='accept', receivers=user, is_received=True, is_accept=True))
        year_earning = 0
        for year_earn in this_year_earning_obj:
            year_earning += year_earn.amount
        return 
    
    # current user totals earnings
    def totals_earning(self, user):
        totals_earning_obj = PaymentProjectBased.objects.filter(Q(project__accept_status='accept') & Q(receivers=user) & Q(is_received=True, is_accept=True))
        totals_earning = 0
        for worker in totals_earning_obj:
            totals_earning += worker.amount
        return totals_earning