from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from .forms import *



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

def deletelist(request,pk):
    item = listapp.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'todoapp/delete.html',context)
