from multiprocessing import context
from django.shortcuts import render
from .models import Task
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    db_data=Task.objects.all()
    context={
        "db_data":db_data[::-1],
        "update":None
    }
    #return HttpResponse("Hola, esta es mi primer vista de django")
    return render(request,"app/index.html",context)

def insert(request):
    try:
        task_subject=request.POST["subject"]
        task_description=request.POST["description"]
        if task_subject=="" or task_description=="":
            raise ValueError("El texto no puede ser vacio")
        db_data=Task(subject=task_subject,description=task_description)
        db_data.save()
        return HttpResponseRedirect(reverse("index"))
    except ValueError as err:
        print(err)
        return HtppResponseRedirect(reverse("index"))

def update(request):
    task_id=request.POST["id"]
    task_subject=request.POST["subject"]
    task_description=request.POST["description"]
    db_data=Task.objects.get(pk=task_id)
    db_data.subject=task_subject
    db_data.description=task_description
    db_data.save()
    return HttpResponseRedirect(reverse("index"))

def update_form(request,task_id):
    db_data=Task.objects.all()
    db_data_only=Task.objects.get(pk=task_id)
    context={
        "db_data":db_data[::-1],
        "update":db_data_only
    }
    return render(request,"app/index.html",context)

def delete(request,task_id):
    db_data=Task.objects.filter(id=task_id)
    db_data.delete()
    return HttpResponseRedirect(reverse("index"))