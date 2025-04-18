from django.shortcuts import render

def home(request):
    template_name = 'homepage/base.html'
    return render(request, template_name )