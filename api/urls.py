from django.urls import path
from . import views

urlpatterns = [
    path('auth/register/', views.RegisterView, name='register'),
    path('auth/login/', views.LoginView, name='login'),
    path('services/', views.ServiceListView, name='service-list'),
]
