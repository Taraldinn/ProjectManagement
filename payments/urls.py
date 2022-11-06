from django.urls import path
from payments import views

app_name = "payments"
urlpatterns = [
    path('worker/', views.PaymentWorkerTemplateView.as_view(), name='payment_worker'),
]
