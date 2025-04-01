from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #Ruta principal
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('task/', views.task),
    path('create_task/', views.create_task)
]