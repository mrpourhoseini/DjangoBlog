from django.contrib import admin, messages
from django.utils.translation import ngettext

from apps.blog.models import Category, Post, Comment, Tag


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.action(description="Mark selected posts as published")
def make_published(self, request, queryset):
    updated = queryset.update(status="Publish")
    self.message_user(request, ngettext(
        '%d post was successfully marked as published.',
        '%d posts were successfully marked as published.',
        updated,
    ) % updated, messages.SUCCESS)


@admin.action(description="Mark selected posts as drafted")
def make_draft(self, request, queryset):
    updated = queryset.update(status="Draft")
    self.message_user(request, ngettext(
        '%d post was successfully marked as drafted.',
        '%d posts were successfully marked as drafted.',
        updated,
    ) % updated, messages.SUCCESS)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'category_to_str', 'slug', 'thumbnail', 'status')
    list_filter = ('author', 'status', 'published_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-published_at']
    actions = [make_published, make_draft]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(status=True)
        return super(PostAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


@admin.action(description="Mark selected comments as published")
def approve_comments(self, request, queryset):
    updated = queryset.update(published=True)
    self.message_user(request, ngettext(
        '%d comment was successfully marked as published.',
        '%d comments were successfully marked as published.',
        updated,
    ) % updated, messages.SUCCESS)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content', 'created_at', 'published')
    list_filter = ('published', 'created_at')
    search_fields = ('post', 'user', 'content')
    actions = [approve_comments]


@admin.register(Tag)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')