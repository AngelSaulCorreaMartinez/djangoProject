from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #Ruta principal
    path('about/', views.about, name='about'),
    path('hello/<str:username>', views.hello, name='hello'),
    path('projects/', views.projects, name='projects'),
    path('project_detail/<int:id>', views.project_detail, name='project_detail'),
    path('task/', views.task, name='task'),
    path('create_task/', views.create_task, name='create_task'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),
    path('task_done_status/<int:id>', views.task_done_status, name='task_done_status'),
    path('create_project/', views.create_project, name='create_project')
]