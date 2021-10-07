from django.urls import path
from . import views

urlpatterns = [
    path('', views.riskRegister, name="riskRegister"),
    path('submission/', views.submission, name="submission")
    ]
# Create your views here.
