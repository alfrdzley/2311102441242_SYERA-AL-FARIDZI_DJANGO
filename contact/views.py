from django.shortcuts import render

def contact(request):
    template_name = 'contact/index.html'
    return render(request, template_name)