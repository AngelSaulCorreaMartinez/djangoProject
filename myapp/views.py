from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def hello(request, username):
    return HttpResponse('<h1>Hello %s</h1>' %username)

# def projects(request):
#     projects = list(Project.objects.values())#Query-Set
#     return JsonResponse(projects, safe=False) #Mandamos en forma de json

def projects(request):
    return render(request, 'projects.html')

# def task(request, id):
#     task = get_object_or_404(Task, id=id) #Obtener objeto, si no, error 404
#     return HttpResponse('task: %s' % task.title)

def task(request):
    return render(request, 'task.html')