from django.shortcuts import render, redirect, HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect !")

    return render(request, 'loginpage.html')

@login_required(login_url = 'login')
def logoutPage(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')

    return render(request, 'register.html')


@login_required(login_url = 'login')
def home(request):
    task = Task.objects.all()
    context = {"task":task}
    return render(request, 'home.html', context)


@login_required(login_url = 'login')
def task(request, pk):
    task = Task.objects.get(id = pk)
    context = {"task":task}
    return render(request, 'task.html', context)


@login_required(login_url = 'login')
def createTask(request):
    form = TaskForm()
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}

    return render(request, 'create_task.html', context)


@login_required(login_url = 'login')
def updateTask(request, pk):
    task = Task.objects.get(id = pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'create_task.html', context)


@login_required(login_url = 'login')
def delete_task(request, pk):
    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')

    return render(request, 'delete_task.html', {'obj':task})