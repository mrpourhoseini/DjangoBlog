from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.html import format_html


def get_superuser():
    su_user = User.objects.filter(is_superuser=True).first()
    if su_user:
        return su_user
    else:
        return "Admin"


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=75, unique=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    objects = CategoryManager()


class Tag(models.Model):
    title = models.CharField(max_length=75, unique=True)
    slug = models.SlugField(max_length=100)
    content = models.TextField(max_length=400)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Post(models.Model):
    STATUS_CHOICES = (
        ("Publish", "published post"),
        ("Draft", "Drafted post")
    )
    author = models.ForeignKey(User, on_delete=models.SET(get_superuser), related_name="posts")
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    summary = models.TextField()
    content = models.TextField()
    tag = models.ManyToManyField(Tag, null=True, blank=True)
    thumbnail = models.ImageField(upload_to="images/", null=True, blank=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def thumbnail_tag(self):
        return format_html(f"<img width=100 height=70 style='border-radius: 5px;' src='{self.thumbnail.url}'>")

    def category_to_str(self):
        return "، ".join([category.title for category in self.category.active()])

    category_to_str.short_description = "Category"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userComments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postComments')
    published = models.BooleanField(default=False)
    content = models.TextField(max_length=400)
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} commented for {self.post.title} : {self.content[:20]}'

    class Meta:
        ordering = ('-created_at',)
