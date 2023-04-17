from django.shortcuts import render
from .models import Task

# Create your views here.


def main(request):
    # для конкретного юзера можно вот так
    # tasks = Task.objects.filter(user=request.user)
    tasks = Task.objects.all()
    
    
    return render(request, 'index.html', context={
        'tasks': tasks
    })
