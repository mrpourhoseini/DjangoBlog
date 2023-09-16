from django.db.models import Count
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post, Comment, Category


# Create your views here.
def home(request):
    posts = Post.objects.filter(status='Publish')[:3]
    authors = User.objects.all()[:5]
    categories = Category.objects.filter(status=True).annotate(num_posts=Count('post')).order_by('-num_posts')[:10]

    context = {
        'posts': posts,
        'authors': authors,
        'categories': categories

    }

    return render(request, 'blog/home.html', context)


def all_posts(request):
    posts = Post.objects.filter(status='Publish')

    context = {
        'posts': posts
    }

    return render(request, 'blog/posts.html', context)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    last_posts = Post.objects.filter(status='Publish')[:5]
    comments = Comment.objects.filter(post__slug=slug, published=True)

    context = {
        'post': post,
        'last_posts': last_posts,
        'comments': comments
    }

    return render(request, 'blog/post.html', context)
