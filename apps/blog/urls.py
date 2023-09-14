from django.urls import path
from .views import all_posts, post_detail

urlpatterns = [
    path('', all_posts, name='all_post'),
    path('posts/<slug:slug>/', post_detail, name='post_detail'),
]