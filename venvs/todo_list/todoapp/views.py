from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo
from .forms import TodoForm
# Create your views here.


def index(request):
    completed = request.GET.get('completed') or False
    todos = Todo.objects.filter(completed=completed)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
    else:
        form = TodoForm()
    
    context = {
        'form': form,
        'todos': todos,
    }
    return render(request, 'todoapp/index.html', context)


def complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todos:index')

def edit(request):
    completed = request.GET.get('completed') or False
    todos = Todo.objects.filter(completed=completed)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
    else:
        form = TodoForm(instance=todo)
    
    context = {
        'form': form,
        'todos': todos,
    }
    return render(request, 'todoapp/index.html', context)