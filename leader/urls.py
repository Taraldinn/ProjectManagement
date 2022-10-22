from django.urls import path
from leader import views

app_name = 'leader'
urlpatterns = [
    path('dashboard/', views.LeaderDashboardAPIView.as_view(), name='leader_dashboard'),
    path('dashboard/worker/', views.WorkerListTemplateAPIView.as_view(), name='leader_worker'),
    path('dashboard/worker/new/', views.CreateWorkerTemplateAPIView.as_view(), name='leader_worker_create'),
]
