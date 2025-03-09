from django.shortcuts import render

def home(request):
    template_name = 'portfolio/home.html'
    context = {
        'title': 'Home',
        'subtitle': 'Syera Al-Faridzi',
        'body': 'Halaman Utama'
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'portfolio/about.html'
    context = {
        'title': 'About',
        'subtitle': 'Syera Al-Faridzi',
        'body': 'Halaman Tentang Saya'
    }
    return render(request, template_name, context)

def contact(request):
    template_name = 'portfolio/contact.html'
    context = {
        'title': 'Contact',
        'subtitle': 'Syera Al-Faridzi',
        'body': 'Halaman Kontak'
    }
    return render(request, template_name, context)

def tools(request):
    template_name = 'portfolio/tools.html'
    context = {
        'title': 'Tools',
        'subtitle': 'Syera Al-Faridzi',
        'body': 'Halaman Tools'
    }
    return render(request, template_name, context)