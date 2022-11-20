
from django.urls import path
from projects import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>', views.project, name='project'),
    path('project-form/', views.project_form, name='project-form'),
    path('update-form/<str:pk>/', views.update_form, name='update-form'),
    path('delete-project/<str:pk>', views.delete_temp, name='delete-project'),
]
