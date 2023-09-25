from django.urls import path
from apps.blog.views import all_posts, post_detail, home, all_category, category_detail, search

urlpatterns = [
    path('', home, name='home'),
    path('posts/', all_posts, name='all_post'),
    path('posts/<slug:slug>/', post_detail, name='post_detail'),
    path('categories/', all_category, name='all_category'),
    path('categories/<slug:slug>/', category_detail, name='category_detail'),
    path('search/', search, name='search')
]