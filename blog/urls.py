from django.urls import path
from blog.views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
]