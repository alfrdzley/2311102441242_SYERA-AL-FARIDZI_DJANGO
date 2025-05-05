from django.shortcuts import render

def projects(request):
    template_name = 'projects/index.html'
    return render(request, template_name)