from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from projects.models import Project, Task, TaskSubmission

User = get_user_model()

# leader dashboard index
class LeaderDashboardAPIView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # admin access
            if request.user.user_type == 'admin':
                return redirect('admin_dashboard:admin_dashboard')

            # leader access
            elif request.user.user_type == 'leader':
                # count area
                leaders_count = User.objects.filter(user_type = 'worker').count()
                projects_count = Project.objects.filter(is_active = True).count()
                tasks_count = Task.objects.filter(is_active = True).count()
                submission_task_count = TaskSubmission.objects.all().count()

                # object filter area
                lates_active_project = Project.objects.filter(is_active=True).order_by('-id')

                context = {
                    'leader_count': leaders_count,
                    'projects_count': projects_count,
                    'tasks_count': tasks_count,
                    'submission_task_count': submission_task_count,
                    'lates_active_project': lates_active_project
                }
                return render(request, 'leader/index.html', context)
            
            # worker access
            elif request.user.user_type == 'worker':
                return redirect('worker:worker_dashboard')
            else:
                return redirect('accounts:login')
        
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        pass


# worker list view
class WorkerListTemplateAPIView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # admin access
            if request.user.user_type == 'admin':
                return redirect('admin_dashboard:admin_dashboard')

            # leader access
            elif request.user.user_type == 'leader':
                
                context = {
                    
                }
                return render(request, 'leader/worker.html', context)
            
            # worker access
            elif request.user.user_type == 'worker':
                return redirect('worker:worker_dashboard')
            else:
                return redirect('accounts:login')
        
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        pass

# worker creation view
# worker list view
class CreateWorkerTemplateAPIView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # admin access
            if request.user.user_type == 'admin':
                return redirect('admin_dashboard:admin_dashboard')

            # leader access
            elif request.user.user_type == 'leader':
                
                context = {
                    
                }
                return render(request, 'leader/new_worker.html', context)
            
            # worker access
            elif request.user.user_type == 'worker':
                return redirect('worker:worker_dashboard')
            else:
                return redirect('accounts:login')
        
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        pass