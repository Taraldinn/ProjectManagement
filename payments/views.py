from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from payments.forms import PaymentProjectBasedForm
from payments.models import PaymentProjectBased
from projects.models import Project


# payment worker creation view
class PaymentWorkerTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # redirect to user dashboard
            if request.user.user_type == 'admin':
                return redirect('admin_dashboard:admin_dashboard')
            elif request.user.user_type == 'leader':
                form = PaymentProjectBasedForm()
                context = {
                    'form': form
                }
                return render(request, 'payments/payment_worker.html', context)
            elif request.user.user_type == 'worker':
                return redirect('worker:worker_dashboard')
            else:
                return redirect('accounts:login')
        else:
            return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.method == 'post' or request.method == 'POST':
                # here will execude tasks
                project_id = request.GET.get('pay_for')
                project_obj = Project.objects.get(id=project_id)
                form = PaymentProjectBasedForm(request.POST, request.FILES)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.project = project_obj
                    instance.sender = request.user
                    instance.save()
                    for worker in request.POST.getlist('receivers'):
                        instance.receivers.add(worker)
                    return redirect('leader:leader_project')
                else:
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # return the same page if run this (else) conditon

        else:
            return redirect('accounts:login')

