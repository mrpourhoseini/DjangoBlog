from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from apps.blog.models import Post


# Create your views here.
def all_author(request):
    authors = User.objects.all()

    context = {
        'authors': authors
    }

    return render(request, 'blog/authors.html', context)


def author_detail(request, user_id):
    author = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(author=author)

    context = {
        'author': author,
        'posts': posts
    }

    return render(request, 'blog/author.html', context)