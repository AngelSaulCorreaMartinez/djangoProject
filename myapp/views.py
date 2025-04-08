from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    title = 'Django Course!'
    return render(request, 'index.html', {'title': title})


def about(request):
    username = 'kat'
    return render(request, 'about.html', {'username': username})


def hello(request, username):
    return HttpResponse('<h1>Hello %s</h1>' % username)

# def projects(request):
#     projects = list(Project.objects.values())#Query-Set
#     return JsonResponse(projects, safe=False) #Mandamos en forma de json


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

# def task(request, id):
#     task = get_object_or_404(Task, id=id) #Obtener objeto, si no, error 404
#     return HttpResponse('task: %s' % task.title)


def task(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task.html', {
        'tasks': tasks
    })

def task_done_status(request, id):
    if request.method == 'POST':
         task = get_object_or_404(Task, id=id)
         task.done = not task.done
         task.save()
         return redirect('task')

def create_task(request):
    if request.method == 'GET':
        # Show interface
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('task')
    
def delete_task(request, id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id)
        task.delete()
        return redirect('task')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        project = Project.objects.create(name=request.POST['name'])
        print(project)
        return redirect('projects')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id )
    return render(request, 'projects/detail.html', {
        'project':project,
        'tasks': tasks
    }) 