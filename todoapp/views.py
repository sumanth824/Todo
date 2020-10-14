from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def logout(request):
    auth.logout(request)
    return redirect('login')
    
def login(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = auth.authenticate(username=u,password=p)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'todoapp/login.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'email is already taken by others')
                return redirect('register')
            elif User.objects.filter(username = uname):
                messages.warning(request, 'Username is taken by others')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=fname,last_name=lname,username = uname, email = email, password=password1,)
                return redirect('home')
        else:
            messages.warning(request, 'passwords not matching')
            return redirect('register')
        
    else:
        return render(request, 'todoapp/register.html')

@login_required(login_url= 'login')
def home(request):
    
    passall =  listapp.objects.all()
    form = listform()
    if request.method == 'POST':
        form = listform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'pass' : passall, 'form': form}
    return render(request, 'todoapp/home.html', context)

@login_required(login_url= 'login')
def updatelist(request, pk):
    task = listapp.objects.get(id=pk)
    form = listform(instance=task)
    if request.method == 'POST':
        form = listform(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'todoapp/update.html',context)

@login_required(login_url= 'login')
def deletelist(request,pk):
    item = listapp.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'todoapp/delete.html',context)
