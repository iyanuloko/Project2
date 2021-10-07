from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path(r'', views.index, name="index"),
    path('logout/', views.logoutUser, name="logout"),
    path('contact/', views.contact, name="contact"),
    ]