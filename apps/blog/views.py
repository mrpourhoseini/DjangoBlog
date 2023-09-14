from django.shortcuts import render
from .models import Post


# Create your views here.
def all_posts(request):
    posts = Post.objects.filter(status='Publish')

    context = {
        'posts': posts
    }

    return render(request, 'blog/posts.html', context)
