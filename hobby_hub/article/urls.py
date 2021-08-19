from django.conf.urls.static import static
from django.urls import path

from hobby_hub import settings
from hobby_hub.article.views import index, create_article, edit_article, delete_article, article_details, \
    article_like, article_dislike, CommentArticleView

urlpatterns=[
    path('', index, name='index'),
    path('details/<int:pk>', article_details, name='article details'),
    path('like/<int:pk>', article_like, name='article likes'),
    path('dislike/<int:pk>', article_dislike, name='article dislikes'),
    path('create/', create_article, name='create article'),
    path('edit/<int:pk>', edit_article, name='edit article'),
    path('delete/<int:pk>', delete_article, name='delete article'),
    path('comment/<int:pk>', CommentArticleView.as_view(), name='comment article'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)