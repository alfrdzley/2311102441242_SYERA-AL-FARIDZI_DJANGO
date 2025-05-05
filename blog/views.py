from django.shortcuts import render
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


# def blog_detail(request):
#     blog_data = Post.objects.all()
#     templates_name = "blog/detail.html"
#
#     return render(request, 'blog/detail.html', {'post': post})

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
