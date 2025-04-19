from django.shortcuts import render

def projects(request):
    template_name = 'projects/base.html'
    return render(request, template_name)