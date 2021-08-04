from django.contrib import admin

# Register your models here.
from hobby_hub.article.models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

