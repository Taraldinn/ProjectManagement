from django.shortcuts import redirect, render

from django.views.generic import TemplateView
from projects.models import Categories, Project, Task, TaskSubmission

class WorkerDashboardTemplateAPIView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == 'admin':
                return redirect('admin_dashboard:admin_dashboard')
            elif request.user.user_type == 'leader':
                return redirect('leader:leader_dashboard')
            elif request.user.user_type == 'worker':
                worker_project = Project.objects.filter(worker=request.user)
                print('=========================')
                print(worker_project)
                print('=========================')
                context = {

                }
                return render(request, 'worker/index.html', context)
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        pass
