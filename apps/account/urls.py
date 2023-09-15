from django.urls import path
from apps.account.views import all_author, author_detail

urlpatterns = [
    path('authors/', all_author, name='all_author'),
    path('authors/<int:user_id>/', author_detail, name='author_detail'),
]