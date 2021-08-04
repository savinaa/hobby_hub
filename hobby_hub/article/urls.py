from django.urls import path

from hobby_hub.article.views import index, create_article

urlpatterns=[
    path('', index, name='index'),
    path('create/', create_article, name='create article'),
]