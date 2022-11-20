from django.shortcuts import render, redirect
from .models import Projects
from .form import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from .utils import search_projects, pagination_projects
from django.contrib import messages


# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


# @login_required(login_url='login')
def projects(request):
    # profile = request.user.profiles
    # p = Projects.objects.all()
    # page = request.GET.get('page')
    # results = 3
    # paginator = Paginator(projects, results)
    #
    # try:
    #     projects = paginator.page(page)
    #
    # except PageNotAnInteger:
    #     page = 1
    #     projects = paginator.page(page)
    #
    # except EmptyPage:
    #     page = paginator.num_pages
    #     projects = paginator.page(page)

    projects, search_query = search_projects(request)
    projects, custom_range = pagination_projects(request, projects, 3)
    return render(request, 'projects.html', {'projects': projects, 'search_query': search_query,
                                             'custom_range':custom_range})


# @login_required(login_url='login')
def project(request, pk):
    # profile = request.user.profiles
    project_object = Projects.objects.get(id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.projects = project_object
        review.owner = request.user.profiles
        review.save()
        messages.success(request, 'Review added successfully!!')

        project_object.get_vote_count

        # project_id =

        return redirect('project', pk=project_object.id)

    context = {'project': project_object, 'form': form}
    return render(request, 'project.html', context)


@login_required(login_url='login')
def project_form(request):
    profile = request.user.profiles
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'create-form.html', context)


@login_required(login_url='login')
def update_form(request, pk):
    profile = request.user.profiles
    up_project = profile.projects_set.get(id=pk)
    form = ProjectForm(instance=up_project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=up_project)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'create-form.html', context)


@login_required(login_url='login')
def delete_temp(request, pk):
    del_project = Projects.objects.get(id=pk)
    if request.method == 'POST':
        del_project.delete()
        return redirect('account')

    context = {'object': del_project}
    return render(request, 'delete-templates.html', context)


