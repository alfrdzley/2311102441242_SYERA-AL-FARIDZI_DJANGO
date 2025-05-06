from django.shortcuts import render, get_object_or_404
from .models import Post


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
