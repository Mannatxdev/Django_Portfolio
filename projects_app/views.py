from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Project
from .forms import ProjectForm


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})


@login_required
def create_project(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to add projects.")

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()

    return render(request, 'create_project.html', {'form': form})


@login_required
def edit_project(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to edit projects.")

    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'edit_project.html', {'form': form})


@login_required
def delete_project(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to delete projects.")

    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('project_list')

    return render(request, 'delete_project.html', {'project': project})
