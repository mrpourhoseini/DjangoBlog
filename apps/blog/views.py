from django.db.models import Count, Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.contrib import messages
from .models import Post, Comment, Category


# Create your views here.
def home(request):
    posts = Post.objects.filter(status='Publish')[:3]
    authors = User.objects.all()[:5]
    categories = Category.objects.filter(status=True).annotate(num_posts=Count('post')).order_by('-num_posts')[:10]
    comments = Comment.objects.filter(published=True).order_by('-created_at')[:5]

    context = {
        'posts': posts,
        'authors': authors,
        'categories': categories,
        'comments': comments

    }

    return render(request, 'blog/home.html', context)


def all_posts(request):
    posts = Post.objects.filter(status='Publish')

    context = {
        'posts': posts
    }

    return render(request, 'blog/posts.html', context)


@login_required
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    last_posts = Post.objects.filter(status='Publish')[:5]
    comments = Comment.objects.filter(post__slug=slug, published=True)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.published = False
            new_comment.save()
            return redirect('post_detail', post.slug)
    form = CommentForm()

    context = {
        'post': post,
        'last_posts': last_posts,
        'comments': comments,
        'form': form
    }

    return render(request, 'blog/post.html', context)


def all_category(request):
    categories = Category.objects.filter(status=True)

    context = {
        'categories': categories
    }

    return render(request, 'blog/categories.html', context)


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(status='Publish', category=category)

    context = {
        'category': category,
        'posts': posts
    }

    return render(request, 'blog/category.html', context)


def search(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        posts = Post.objects.filter(Q(title__contains=search_query) | Q(category__title__contains=search_query))

        context = {
            'query': search_query,
            'posts': posts
        }

        return render(request, 'blog/search.html', context)
    else:
        return render(request, 'blog/search.html', {})
