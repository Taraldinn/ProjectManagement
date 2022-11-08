from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from django.views.generic import TemplateView
from projects.forms import IssuesModelForm, ProjectSubmissionModelForm, TaskModelForm
from projects.models import Categories, Issues, Project, ProjectSubmission, Task
from django.db.models import Q
from django.contrib import messages
from payments.models import PaymentProjectBased



class WorkerDashboardTemplateAPIView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == 'admin':
                return redirect('admin_dashboard:admin_dashboard')
            elif request.user.user_type == 'leader':
                return redirect('leader:leader_dashboard')
            elif request.user.user_type == 'worker':
                if request.user.profile.is_fully_filled():
                    worker_project = Project.objects.filter(Q(worker=request.user) & Q(status='done'))
                    worker_task = Task.objects.filter(Q(worker=request.user) & Q(status='done'))
                    worker_issues = Issues.objects.filter(Q(project__worker=request.user))
                    
                    worker_earning_obj = PaymentProjectBased.objects.filter(Q(project__accept_status='accept') & Q(receivers=request.user) & Q(is_received=True))
                    worker_earning = 0
                    for worker in worker_earning_obj:
                        worker_earning += worker.amount

                    context = {
                        'worker_project': worker_project,
                        'worker_task': worker_task,
                        'worker_issues': worker_issues,
                        'worker_earning': worker_earning
                    }
                    return render(request, 'worker/index.html', context)
                else:
                    return redirect('accounts:accounts_edit_profile')
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        pass

# project List view
class ProjectListTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_fully_filled():
                # redirect to user dashboard
                if request.user.user_type == 'admin':
                    return redirect('admin_dashboard:admin_dashboard')
                elif request.user.user_type == 'leader':
                    return redirect('leader:leader_dashboard')
                elif request.user.user_type == 'worker':
                    projects = Project.objects.filter(Q(worker=request.user) & Q(is_active = True)).order_by('-id')
                    context = {
                        'projects': projects
                    }
                    return render(request, 'worker/projects.html', context)
                else:
                    return redirect('accounts:login')
            else:
                return redirect('accounts:accounts_edit_profile')
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        pass

# project detials view
class ProjectDetailTemplateView(TemplateView):
    def get(self, request, pk, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_fully_filled():
                # redirect to user dashboard
                if request.user.user_type == 'admin':
                    return redirect('admin_dashboard:admin_dashboard')
                elif request.user.user_type == 'leader':
                    return redirect('leader:leader_dashboard')
                elif request.user.user_type == 'worker':
                    project = Project.objects.get(id=pk)
                    tasks = Task.objects.filter(project=project).order_by('-id')

                    form = ProjectSubmissionModelForm()
                    issues_form = IssuesModelForm()
                    
                    context = {
                        'project': project,
                        'tasks': tasks,
                        'form': form,
                        'issues_form': issues_form
                    }
                    return render(request, 'worker/project_detail.html', context)
                else:
                    return redirect('accounts:login')
            else:
                return redirect('accounts:accounts_edit_profile')
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.method == 'post' or request.method == 'POST':
                # here will execude tasks
                project_id = request.POST.get('project_id')
                project_obj = Project.objects.get(id=project_id)
                postData = {
                    'project': project_obj,
                    'status': request.POST.get('status'),
                    'description': request.POST.get('description'),
                    'file': request.POST.get('file')
                }
                form = ProjectSubmissionModelForm(postData, request.FILES)
                # Issues form submission ======================================
                issues_form = IssuesModelForm(request.POST, request.FILES)

                # Project form submission ======================================
                if form.is_valid():
                    if ProjectSubmission.objects.filter(project=project_id).exists():
                        messages.info(request, "This Project Has Been Submited..!")
                        return redirect('worker:worker_project')
                    else:
                        form.save()
                        ## here will update all {project, task} status to DONE becouse project is submited
                        project_obj.status = 'done'
                        project_obj.complete_per = 100
                        for task in project_obj.tasks.all():
                            task.status = 'done'
                            task.due = 'done'
                            task.save()
                        project_obj.save()
                        ## end updated all info
                        return redirect('worker:worker_project')

                # Issues form submission ======================================
                if issues_form.is_valid():
                    instance = issues_form.save(commit=False)
                    instance.project = project_obj
                    instance.task = None
                    instance.is_active = True
                    instance.save()
                    return redirect('worker:worker_project')
                else:
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # return the same page if run this (else) conditon

        else:
            return redirect('accounts:login')

# project detials view
class AcceptProjectTemplateView(TemplateView):
    def get(self, request, pk, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_fully_filled():
                # redirect to user dashboard
                if request.user.user_type == 'admin':
                    return redirect('admin_dashboard:admin_dashboard')
                elif request.user.user_type == 'leader':
                    return redirect('leader:leader_dashboard')
                elif request.user.user_type == 'worker':
                    project = Project.objects.get(id=pk)
                    project.status = 'working'
                    project.accept_status = 'accept'
                    project.save()
                    payment_obj = PaymentProjectBased.objects.get(project=project)
                    payment_obj.is_received = True
                    payment_obj.save()
                    return redirect('worker:worker_project')
                else:
                    return redirect('accounts:login')
            else:
                return redirect('accounts:accounts_edit_profile')
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        pass

# Task creation and list view
class TaskListTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_fully_filled():
                # redirect to user dashboard
                if request.user.user_type == 'admin':
                    return redirect('admin_dashboard:admin_dashboard')
                elif request.user.user_type == 'leader':
                    return redirect('leader:leader_dashboard')
                elif request.user.user_type == 'worker':
                    tasks = Task.objects.filter(Q(project__worker=request.user) & Q(is_active=True)).order_by('-id')
                    task_issues = Issues.objects.filter(Q(project__worker=request.user) & Q(is_active=True)).order_by('-id')
                    
                    task_form = TaskModelForm()
                    context = {
                        'tasks': tasks,
                        'task_issues': task_issues,
                        'task_form': task_form
                    }
                    return render(request, 'worker/tasks.html', context)
                else:
                    return redirect('accounts:login')
            else:
                return redirect('accounts:accounts_edit_profile')
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.method == 'post' or request.method == 'POST':
                # here will execude tasks
                form = TaskModelForm(request.POST, request.FILES)
                if form.is_valid():
                    instance = form.save()
                    for worker in request.POST.getlist('worker'):
                        instance.worker.add(worker)
                    return redirect('leader:leader_task')
                else:
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # return the same page if run this (else) conditon

        else:
            return redirect('accounts:login')

# Project Submission view
class ProjectSubmissionTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_fully_filled():
                # redirect to user dashboard
                if request.user.user_type == 'admin':
                    return redirect('admin_dashboard:admin_dashboard')
                elif request.user.user_type == 'leader':
                    return redirect('leader:leader_dashboard')
                elif request.user.user_type == 'worker':
                    submited_projects = ProjectSubmission.objects.filter(Q(project__worker=request.user) & Q(project__status='done')).order_by('-id')
                    context = {
                        'submited_projects': submited_projects
                    }
                    return render(request, 'worker/project_submission.html', context)
                else:
                    return redirect('accounts:login')
            else:
                return redirect('accounts:accounts_edit_profile')
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.method == 'post' or request.method == 'POST':
                # here will execude tasks
                pass
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # return the same page if run this (else) conditon

        else:
            return redirect('accounts:login')
