import imp
from django.urls import path
from worker import views

app_name = 'worker'

urlpatterns = [
    path('dashboard/', views.WorkerDashboardTemplateAPIView.as_view(), name='worker_dashboard'),
]
