from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello), #Ruta principal
    path('about/', views.about)
]