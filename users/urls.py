from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('user-profile/<str:pk>', views.user_profile, name='user-profile'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.user_register, name='register'),
    path('account', views.user_account, name='account'),
    path('edit-account/', views.edit_account, name='edit-account'),
    path('skill-form/', views.skill_form, name='skill-form'),
    path('update-skill/<str:pk>', views.edit_skill, name='update-skill'),
    path('delete-skill/<str:pk>', views.delete_skill, name='delete-skill'),
    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>/', views.view_message, name='message'),
    path('create-message/<str:pk>/', views.create_message, name='create-message'),
]
