from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<str:pk>/', views.task, name='task'),

    path('create_task', views.createTask, name='create_task'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete_task/<str:pk>/', views.delete_task, name='delete_task'),

    path('login', views.loginPage, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logoutPage, name='logout'),
]