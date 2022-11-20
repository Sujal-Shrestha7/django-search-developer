from django.shortcuts import render, redirect
from .models import Profiles, Skills
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserCreationForm, AccountForm, SkillForm, CreateMessage
from django.contrib.auth.decorators import login_required
from .utils import search_profiles, pagination_profiles
from django.db.models import Q


# Create your views here.

# @login_required(login_url='login')
def profiles(request):
    # search_query = ''
    # if request.GET.get('search_query'):
    #     search_query = request.GET.get('search_query')
    #
    # skill = Skills.objects.filter(name__icontains=search_query)
    # profiles = Profiles.objects.distinct().filter(Q(name__icontains=search_query) |
    #                                    Q(short_intro__icontains=search_query) |
    #                                    Q(skills__in=skill))
    profiles, search_query = search_profiles(request)
    profiles, custom_range = pagination_profiles(request, profiles, 3)
    context = {'profiles': profiles, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'profiles.html', context)


# @login_required(login_url='login')
def user_profile(request, pk):
    profile = Profiles.objects.get(id=pk)
    top_skills = profile.skills_set.exclude(description__exact='')
    other_skills = profile.skills_set.filter(description__exact='')
    return render(request, 'user_profile.html', {'profiles': profile,
                                                 'top_skills': top_skills, 'other_skills': other_skills})


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exists ')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'User logged in ')
            return redirect(request.GET['next'] if 'next' in request.GET else 'profiles')

        else:
            messages.error(request, 'Username OR Password is incorrect')
    return render(request, 'login_page.html', {'page': page})


def user_register(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.upper()
            user.save()

            messages.info(request, 'User has been registered .')
            login(request, user)
            if request.user.is_authenticated:
                # messages.info(request, 'User has been registered .')
                return redirect('edit-account')
        else:
            messages.error(request, 'Something error occurred during registration .')

    context = {
        'page': page,
        'form': form,

    }
    return render(request, 'login_page.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, 'User logged out .')
    return redirect('login')


@login_required(login_url='login')
def user_account(request):
    profile = request.user.profiles
    skills = profile.skills_set.all()
    projects = profile.projects_set.all()
    context = {'profiles': profile, 'skills': skills, 'projects': projects}
    return render(request, 'account.html', context)


@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profiles
    form = AccountForm(instance=profile)
    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'edit_account.html', context)


@login_required(login_url='login')
def skill_form(request):
    profile = request.user.profiles
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill Added Successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'skill_form.html', context)


@login_required(login_url='login')
def edit_skill(request, pk):
    profile = request.user.profiles
    skill = profile.skills_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated Successfully')
            return redirect('account')
    context = {'form': form}

    return render(request, 'skill_form.html', context)


@login_required(login_url='login')
def delete_skill(request, pk):
    profile = request.user.profiles
    skill = profile.skills_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill Deleted Successfully !!')
        return redirect('account')

    context = {'object': skill}
    return render(request, 'delete-templates.html', context)


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profiles
    message_inbox = profile.messages.all()
    unreadCount = message_inbox.filter(is_read=False).count()
    context = {'message_inbox':message_inbox, 'unreadCount':unreadCount}
    return render(request, 'inbox.html', context)


@login_required(login_url='login')
def view_message(request, pk):
    profile = request.user.profiles
    view_msg = profile.messages.get(id=pk)
    if not view_msg.is_read:
        view_msg.is_read = True
        view_msg.save()
    context = {'message': view_msg}
    return render(request, 'message.html', context)


def create_message(request, pk):
    recipient = Profiles.objects.get(id=pk)
    form = CreateMessage()
    try:
        sender = request.user.profiles
    except:
        sender = None

    if request.method == 'POST':
        form = CreateMessage(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()
            messages.success(request, 'Message sent successfully !!')
            return redirect('user-profile', pk=recipient.id)

    context = {'recipient': recipient, 'form':form}
    return render(request, 'create_message.html', context)
