from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q


def search_projects(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    tag = Tag.objects.filter(name__icontains=search_query)
    project = Projects.objects.distinct().filter(Q(title__icontains=search_query) |
                                                 Q(description__icontains=search_query) |
                                                 Q(owner__name__icontains=search_query) |
                                                 Q(tags__in=tag))
    return project, search_query


def pagination_projects(request, projects, results):
    page = request.GET.get('page')
    projects = projects
    pagination = Paginator(projects, results)
    try:
        projects = pagination.page(page)
    except PageNotAnInteger:
        page = 1
        projects = pagination.page(page)
    except EmptyPage:
        page = pagination.num_pages
        projects = pagination.page(page)

    left_index = (int(page)-4)
    if left_index < 1:
        left_index = 1

    right_index = (int(page)+4)
    if right_index > pagination.num_pages:
        right_index = pagination.num_pages+1

    custom_range = range(left_index, right_index)
    return projects, custom_range
