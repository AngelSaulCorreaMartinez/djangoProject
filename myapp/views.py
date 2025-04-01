from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask

# Create your views here.
def index(request):
    title = 'Django Course!'
    return render(request, 'index.html', {'title':title})

def about(request):
    username = 'kat'
    return render(request, 'about.html', {'username': username})

def hello(request, username):
    return HttpResponse('<h1>Hello %s</h1>' %username)

# def projects(request):
#     projects = list(Project.objects.values())#Query-Set
#     return JsonResponse(projects, safe=False) #Mandamos en forma de json

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects':projects
    })

# def task(request, id):
#     task = get_object_or_404(Task, id=id) #Obtener objeto, si no, error 404
#     return HttpResponse('task: %s' % task.title)

def task(request):
    tasks = Task.objects.all()
    return render(request, 'task.html', {
        'tasks':tasks
    })

def create_task(request):
    if request.method == 'GET':
        #Show interface
        return render(request, 'create_task.html', {
        'form':CreateNewTask()
    })
    else:
            Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
            return redirect('/task/')
