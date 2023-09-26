from django import forms
from django.forms import Textarea
from apps.blog.models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'p-5 w-full text-sm text-gray-900 rounded-lg rounded-t-lg border border-gray-200 dark:bg-gray-800 dark:border-gray-700 focus:ring-0 focus:outline-none dark:text-white dark:placeholder-gray-400 dark:bg-gray-800', 'id': 'comment', 'rows': 6, 'placeholder': 'Write a comment...'}), label='', max_length=400)

    class Meta:
        model = Comment
        fields = ('content',)
