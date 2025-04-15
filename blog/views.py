from django.shortcuts import render

# Create your views here.

def dashboard(request):
    templates_name = "dashboard/index.html"
    context = {
        'title': 'Dashboard',
    }
    return render(request, templates_name, context)