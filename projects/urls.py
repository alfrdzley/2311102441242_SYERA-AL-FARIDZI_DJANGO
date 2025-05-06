from django.urls import path
from projects.views import projects, project_detail

urlpatterns = [
    path('', projects, name='projects'),
    path('detail/<slug:slug>/', project_detail, name='project_detail'),
    path('detail/<int:project_id>/', project_detail, name='project_detail_id'),
]
