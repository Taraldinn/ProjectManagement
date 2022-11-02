import imp
from django.urls import path
from worker import views

app_name = 'worker'

urlpatterns = [
    path('dashboard/', views.WorkerDashboardTemplateAPIView.as_view(), name='worker_dashboard'),
    path('dashboard/project/', views.ProjectListTemplateView.as_view(), name='worker_project'),
    path('dashboard/project/<str:pk>/', views.ProjectDetailTemplateView.as_view(), name='worker_project_detail'),
    path('dashboard/task/', views.TaskListTemplateView.as_view(), name='worker_task'),
    path('dashboard/project/submited/list/', views.ProjectSubmissionTemplateView.as_view(), name='worker_project_submited'),
]
