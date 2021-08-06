from django.conf.urls.static import static
from django.urls import path

from hobby_hub import settings
from hobby_hub.article.views import index, create_article

urlpatterns=[
    path('', index, name='index'),
    path('create/', create_article, name='create article'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)