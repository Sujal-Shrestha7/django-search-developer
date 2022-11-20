
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def search_profiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    skill = Skills.objects.filter(name__icontains=search_query)
    profiles = Profiles.objects.distinct().filter(Q(name__icontains=search_query) |
                                                  Q(short_intro__icontains=search_query)|
                                                  Q(skills__in=skill))

    return profiles, search_query


def pagination_profiles(request, profiles, results):
    page = request.GET.get('page')
    pagination = Paginator(profiles, results)
    try:
        profiles = pagination.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = pagination.page(page)
    except EmptyPage:
        page = pagination.num_pages
        profiles = pagination.page(page)

    left_index = (int(page)-4)
    if left_index < 1:
        left_index = 1

    right_index = (int(page)+4)
    if right_index > pagination.num_pages:
        right_index = pagination.num_pages+1

    custom_range = range(left_index, right_index)
    return profiles, custom_range



