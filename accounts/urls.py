from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('register/leader', views.LeaderRegisterTemplateView.as_view(), name='register_leader'), # leader register route
    path('register/worker', views.WorkerRegisterTemplateView.as_view(), name='register_worker'), # worker register route
    path('', views.LoginTemplateView.as_view(), name='login'), # login page route
]
