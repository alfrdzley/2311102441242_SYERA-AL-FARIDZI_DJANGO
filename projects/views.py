from django.shortcuts import render, get_object_or_404
from .models import Project

def projects(request):
    projects_data = Project.objects.all()
    has_more = projects_data.count() > 3
    template_name = "projects/base.html"
    context = {
        'title': 'Projects',
        'projects': projects_data,
        'has_more': has_more,
        'initial_projects': projects_data[:3],
        'remaining_projects': projects_data[3:] if has_more else [],
    }
    return render(request, template_name, context)

def project_detail(request, slug=None, project_id=None):
    if slug:
        try:
            project = get_object_or_404(Project, slug=slug)
        except:
            # If slug field doesn't exist in the database, fall back to ID
            project = get_object_or_404(Project, id=slug)
    else:
        project = get_object_or_404(Project, id=project_id)

    template_name = "projects/detail.html"
    context = {
        'title': project.title,
        'project': project,
    }
    return render(request, template_name, context)
