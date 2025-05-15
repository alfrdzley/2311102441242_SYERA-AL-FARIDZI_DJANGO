from django.urls import path
from blog.views import blog, dashboard, blog_detail, blog_login

urlpatterns = [
    path('', blog, name='blog'),
    path('dashboard', dashboard, name='dashboard'),
    path('detail/<slug:slug>/', blog_detail, name='blog_detail'),
    path('login/', blog_login, name='login'),
]
