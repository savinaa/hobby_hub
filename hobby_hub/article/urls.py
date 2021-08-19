from django.conf.urls.static import static
from django.urls import path

from hobby_hub import settings
from hobby_hub.article.views import index, create_article, edit_article, delete_article, article_details, \
    url_to_article_like_id, url_to_article_dislike_id

urlpatterns=[
    path('', index, name='index'),
    path('details/<int:pk>', article_details, name='article details'),
    path('like/<int:pk>', url_to_article_like_id, name='article likes'),
    path('dislike/<int:pk>', url_to_article_dislike_id, name='article dislikes'),
    path('create/', create_article, name='create article'),
    path('edit/<int:pk>', edit_article, name='edit article'),
    path('delete/<int:pk>', delete_article, name='delete article'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)