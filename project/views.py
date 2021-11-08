from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from pprint import pprint
from django.contrib.auth.decorators import login_required


def projects(request):
    projects = Project.objects.all()
    return render(request, "project/projects.html", {"projects": projects})


def project(request, pk):
    project = Project.objects.get(slug=pk)
    return render(request, "project/project.html", {"project": project})


@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, "project/form.html", {'form': form})


@login_required(login_url='login')
def updateProject(request, pk):
    project = Project.objects.get(slug=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        pprint(request.FILES)
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, "project/form.html", {'form': form})


@login_required(login_url='login')
def deleteProject(request, pk):
    project = Project.objects.get(slug=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    return render(request, "project/delete.html", {"project": project})
