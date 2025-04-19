from django.shortcuts import render

def about(request):
    template_name = 'about/base.html'
    return render(request, template_name)