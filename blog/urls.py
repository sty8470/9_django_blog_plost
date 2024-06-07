from django.urls import path
from django.views.generic import TemplateView
from .views import BlogPostListCreate, BlogPostRetrieveUpdateDestroy

urlpatterns = [
    path('posts/', BlogPostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogPostRetrieveUpdateDestroy.as_view(), name='post-detail'),
]
