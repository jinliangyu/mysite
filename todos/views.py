from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

# Create your views here.
def index(request):
    # return HttpResponse('This is todos!')
    todos = Todo.objects.all()[:10]
    context = {
        'todos': todos,
        'name': 'jly'
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)
    context={
        'todo': todo,
    }
    return render(request , 'details.html' , context)