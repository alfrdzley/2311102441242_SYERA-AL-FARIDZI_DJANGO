from django.contrib import messages

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


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


def blog_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if User.objects.create_user(username=username, password=password, email=email):
            messages.success(request, 'User created successfully')
            return redirect('login')
        else:
            messages.error(request, 'User creation failed')
    else:
        messages.error(request, 'Invalid request method')
    return render(request, 'blog/signup.html')


def logout_view(request):
    logout(request)
    return redirect('login')
