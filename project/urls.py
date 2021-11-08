from django.urls import path
from . import views
urlpatterns = [
    path("projects/", views.projects, name="projects"),
    path("projects/<str:pk>/", views.project, name="project"),
    path("projects/create", views.createProject, name="createProject"),
    path("projects/update/<str:pk>/", views.updateProject, name="updateProject"),
    path("projects/delete/<str:pk>/", views.deleteProject, name="deleteProject"),
]
