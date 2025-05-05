from django import views
from django.urls import path

from blog.views import blog, dashboard

urlpatterns = [
    path('', blog, name='blog'),
    path('dashboard', dashboard, name='dashboard'),
    # path('detail/<int:pk>', blog_detail, name='blog_detail'),
    # path('new', create_post, name='create_post'),
    # path('<int:pk>/', post_detail, name='post_list'),
    # path('<int:pk>/update/', update_post, name='update_post'),
    # path('<int:pk>/delete/', delete_post, name='delete_post'),
]