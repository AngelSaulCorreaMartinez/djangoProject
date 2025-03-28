from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse('Index Page')

def hello(request, username):
    return HttpResponse('<h1>Hello %s</h1>' %username)

def about(request):
    return HttpResponse('<h2>About</h2>')

def projects(request):
    projects = list(Project.objects.values())#Query-Set
    return JsonResponse(projects, safe=False) #Mandamos en forma de json

def task(request, id):
    task = get_object_or_404(Task, id=id) #Obtener objeto, si no, error 404
    return HttpResponse('task: %s' % task.title)