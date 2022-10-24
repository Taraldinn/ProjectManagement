from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from projects.models import Project, Task, TaskSubmission
from accounts.forms import RegisterForm

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
                ongoing_projects = Project.objects.filter(is_active=True).order_by('-id')

                context = {
                    'leader_count': leaders_count,
                    'projects_count': projects_count,
                    'tasks_count': tasks_count,
                    'submission_task_count': submission_task_count,
                    'ongoing_projects': ongoing_projects
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
                workers = User.objects.filter(user_type='worker').order_by('-id')
                context = {
                    'workers': workers
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
        if request.user.is_authenticated:
            # admin access
            if request.user.user_type == 'admin':
                return redirect('admin_dashboard:admin_dashboard')
            # leader access
            elif request.user.user_type == 'leader':
                email = request.POST.get('email')
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')
                formData = {
                    'email': email,
                    'password1': password1,
                    'password2': password2
                }
                form = RegisterForm(formData)
                
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.user_type = 'worker'
                    instance.is_active = True
                    instance.save()
                    return redirect('leader:leader_worker')
                
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



# project view
class ProjectTemplateAPIView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # redirect to user dashboard
            if request.user.user_type == 'admin':
                return redirect('admin_dashboard:admin_dashboard')
            elif request.user.user_type == 'leader':
                projects = Project.objects.all().order_by('-id')
                context = {
                    'projects': projects
                }
                return render(request, 'leader/project.html', context)
            elif request.user.user_type == 'worker':
                return redirect('worker:worker_dashboard')
            else:
                return redirect('accounts:login')
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        pass