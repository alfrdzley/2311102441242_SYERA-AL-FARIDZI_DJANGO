from django.shortcuts import render, get_object_or_404
from .models import Post


def dashboard(request):
    templates_name = "dashboard/index.html"
    context = {
        'title': 'Dashboard',
    }
    return render(request, templates_name, context)


def projects(request):
    return None


def blog(request):
    blog_data = Post.objects.all()
    has_more = blog_data.count() > 3
    templates_name = "blog/base.html"
    context = {
        'title': 'Blog',
        'posts': blog_data,
        'has_more': has_more,
        'initial_posts': blog_data[:3],
        'remaining_posts': blog_data[3:] if has_more else [],
    }
    return render(request, templates_name, context)


def blog_detail(request, slug=None, post_id=None):
    if slug:
        try:
            post = get_object_or_404(Post, slug=slug)
        except:
            # If slug field doesn't exist in the database, fall back to ID
            post = get_object_or_404(Post, id=slug)
    else:
        post = get_object_or_404(Post, id=post_id)

    templates_name = "blog/detail.html"
    context = {
        'title': post.title,
        'post': post,
    }
    return render(request, templates_name, context)

#
# # Create
# def create_post(request):
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = BlogPostForm()
#     return render(request, 'blog/create_post.html', {'form': form})
#
#
# # Read
# def post_list(request):
#     posts = blog.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})
#
#
# def post_detail(request, pk):
#     post = get_object_or_404(blog, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})
#
#
# # Update
# def update_post(request, pk):
#     post = get_object_or_404(blog, pk=pk)
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = BlogPostForm(instance=post)
#     return render(request, 'blog/update_post.html', {'form': form})
#
#
# # Delete
# def delete_post(request, pk):
#     post = get_object_or_404(blog, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#     return render(request, 'blog/delete_post.html', {'post': post})
