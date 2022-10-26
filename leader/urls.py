from django.urls import path
from leader import views

app_name = 'leader'
urlpatterns = [
    path('dashboard/', views.LeaderDashboardAPIView.as_view(), name='leader_dashboard'),
    path('dashboard/worker/', views.WorkerListTemplateAPIView.as_view(), name='leader_worker'),
    path('dashboard/project/', views.ProjectListTemplateAPIView.as_view(), name='leader_project'),
    path('dashboard/project/add/', views.ProjectCreateTemplateAPIView.as_view(), name='leader_project_add'),
]
