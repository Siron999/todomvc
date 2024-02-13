from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from .models import Todo
from .forms import TodoForm


def todo(request, pk=None):
    todo = {}
    if pk:
        try:
            todo = [Todo.objects.get(todo_id=pk)]
        except ObjectDoesNotExist as e:
            print(e)
    else:
        todo = Todo.objects.all()
    return render(request, "todoapp/home.html", {"todos": todo})


def add_todo(request):
    todo_form = TodoForm()
    if request.method == "POST":
        todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            todo_form.save()
            return redirect("home")
    return render(request, "todoapp/todoform.html", {"form": todo_form})


def update_todo(request, pk):
    todo = {}
    try:
        todo = Todo.objects.get(todo_id=pk)
    except ObjectDoesNotExist as e:
        print(e)
        return redirect("home")
    todo_form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "todoapp/todoform.html", {"form": todo_form})


def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(todo_id=pk)
    except ObjectDoesNotExist as e:
        print(e)
        return redirect("home")
    if request.method == 'POST':
        todo.delete()
        return redirect("home")
    return render(request, "todoapp/delete.html", {"todo": todo})
