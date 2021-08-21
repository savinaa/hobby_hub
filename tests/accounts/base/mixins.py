from django.contrib.auth import get_user_model

from hobby_hub.article.models import Article, Like

UserModel = get_user_model()


class ArticleTestUtils:
    def create_article(self, **kwargs):
        return Article.objects.create(**kwargs)

    def create_article_with_like(self, like_user, **kwargs):
        article = self.create_article(**kwargs)
        Like.objects.create(
            article=article,
            user=like_user,
        )
        return article


class UserTestUtils:
    def create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)