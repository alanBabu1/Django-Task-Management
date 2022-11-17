from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TaskDetails
from .forms import TaskDetailsForm,SignUpForm,LoginForm,AddTaskForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DeleteView
from django.urls import reverse_lazy


def home(request):
    return render(request, "index.html")


def register(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You are registered Successfully !!!")
            return redirect('login')
    context={'form':form}
    return render(request,"register.html",context=context)


def login(request):
    form=LoginForm
    if request.method=='POST':
        form= LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request, "You are logged in Successfully !!!")
                return redirect('main')
            
    context={'form':form}
    return render(request,"login.html",context=context)


def logout(request):
    auth.logout(request)
    messages.success(request, "You are logged out Successfully !!!")
    return redirect("home")


@login_required(login_url='login')
def mainPage(request):
    return render(request,"main.html")


@login_required(login_url='login')
def create(request):
    form=AddTaskForm(request.POST)
    task=TaskDetails.objects.all()
    
    if request.method =='POST':
        form=AddTaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            form.save()
            messages.success(request, "New task created Successfully !!!")
            return redirect('view')

    context={'form':form}
    return render(request, 'create.html',context=context)


@login_required(login_url='login')
def view(request): 
    current_user = request.user.id
    task=TaskDetails.objects.all().filter(user=current_user)   
    context={'task':task}
    return render(request, 'view.html',context=context)


@login_required(login_url='login')
def assigned(request):  
    task=TaskDetails.objects.filter(task_owner=request.user)
    context={'task':task}
    return render(request,'assigned.html',context=context)


@login_required(login_url='login')
def update(request,pk):
    task=TaskDetails.objects.get(id=pk)
    form= AddTaskForm(request.POST or None,instance=task)
    if request.method=='POST':
        form= AddTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated Successfully !!!")
            return redirect('view')
    context={'form':form}
    return render(request, 'update.html',context=context)


@login_required(login_url='login')
def delete(request,pk):
    task=TaskDetails.objects.get(id=pk)   
    if request.method=='POST':
        task.delete()
        messages.success(request, "Task Deleted Successfully !!!")
        return redirect('assigned')
    
    context={'object':task}
    return render(request, 'delete.html',context=context)

