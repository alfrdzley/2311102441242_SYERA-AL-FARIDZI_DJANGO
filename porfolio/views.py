from django.shortcuts import render

def home(request):
    template_name = 'portfolio/home.html'
    context = {
        'title': 'Syera Al-Faridzi',
        'subtitle': 'Mau Jadi Software Engineer',
        'body': 'Halaman Utama'
    }
    return render(request, template_name, context)