from django.urls import path
from apps.blog.views import all_posts, post_detail, home

urlpatterns = [
    path('', home, name='home'),
    path('posts/', all_posts, name='all_post'),
    path('posts/<slug:slug>/', post_detail, name='post_detail'),
]