from django.shortcuts import render
from .models import Post


# Create your views here.
def all_posts(request):
    posts = Post.objects.filter(status='Publish')

    context = {
        'posts': posts
    }

    return render(request, 'blog/posts.html', context)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    last_posts = Post.objects.filter(status='Publish')[:5]

    context = {
        'post': post,
        'last_posts': last_posts
    }

    return render(request, 'blog/post.html', context)
