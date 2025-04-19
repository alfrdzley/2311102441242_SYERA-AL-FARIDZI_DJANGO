from django.shortcuts import render

def contact(request):
    template_name = 'contact/base.html'
    return render(request, template_name)