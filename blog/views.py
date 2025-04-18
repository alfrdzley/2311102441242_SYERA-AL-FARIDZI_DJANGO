from django.shortcuts import render

def blog(request):
    templates_name = "blog/base.html"

def dashboard(request):
    templates_name = "dashboard/index.html"
    context = {
        'title': 'Dashboard',
    }
    return render(request, templates_name, context)