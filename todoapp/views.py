from django.http import Http404, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Todo
from .forms import TodoForm


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(request.user)
            return redirect("home")
        messages.error(request, "Invalid Credential")
    return render(request, "todoapp/login.html")


def logout_action(request):
    if request.method == 'POST':
        logout(request)
        return redirect("login")
    raise Http404()


def register_action(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, "todoapp/register.html", {"form": form})


@login_required(login_url='login')
def todo(request, pk=None):
    todo = {}
    if pk:
        try:
            todo = [Todo.objects.get(todo_id=pk)]
        except ObjectDoesNotExist as e:
            print(e)
    else:
        todo = Todo.objects.filter(user__username=request.user.username)
    return render(request, "todoapp/home.html", {"todos": todo})


@login_required(login_url='login')
def add_todo(request):
    print(Todo.todo_id)
    user = request.user
    todo_form = TodoForm()
    if request.method == "POST":
        todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            todo = todo_form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect("home")
    return render(request, "todoapp/todoform.html", {"form": todo_form})


@login_required(login_url='login')
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


@login_required(login_url='login')
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
