from pyexpat.errors import messages

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


@login_required
def dashboard(request):
    templates_name = "dashboard/index.html"
    context = {
        'title': 'Dashboard',
    }
    return render(request, templates_name, context)


def blog(request):
    blog_data = Post.objects.all()
    templates_name = "blog/base.html"
    context = {
        'title': 'Blog',
        'posts': blog_data,
    }
    return render(request, templates_name, context)


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    templates_name = "blog/detail.html"
    context = {
        'title': post.title,
        'post': post,
    }
    return render(request, templates_name, context)


def blog_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'blog/login.html')
