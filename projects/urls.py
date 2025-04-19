from django.urls import path
from projects.views import projects

urlpatterns = [
    path('', projects, name='projects'),
]