from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profiles, Skills, Message


# from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
            'email': 'Email',
            'username': 'Username',
            'password1': 'password',
            'password2': 'confirm password'

        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class AccountForm(ModelForm):
    class Meta:
        model = Profiles
        fields = ['name', 'email', 'username', 'profile_image', 'bio', 'location',
                  'short_intro', 'social_github', 'social_linkedin', 'social_twitter', 'social_stackoverflow',
                  'social_website']

        labels = {
            'name': 'Name',
            'email': 'Email',
            'username': 'Username',
            'profile_image': 'Profile Image',
            'bio': 'Short Bio',
            'location': 'Address',
            'short_intro': 'Short Intro',
            'social_github': 'Github Link',
            'social_linkedin': 'LinkedIn Link',
            'social_twitter': 'Twitter',
            'social_stackoverflow': 'StackOverFlow',
            'social_website': 'Website Link',
        }

        # exclude = ['user']
        # widgets = {
        #     'user': forms.RadioSelect(),
        # }

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class CreateMessage(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super(CreateMessage, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
