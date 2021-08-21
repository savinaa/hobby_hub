from django.urls import reverse

from hobby_hub.article.models import Like
from tests.accounts.base.mixins import ArticleTestUtils, UserTestUtils
from tests.accounts.base.tests import HobbyHubTestCase


class LikeArticleViewTests(ArticleTestUtils, UserTestUtils, HobbyHubTestCase):
    def test_likeArticle__whenArticleNotLiked_shouldCreateLike(self):
        self.client.force_login(self.user)
        article_user = self.create_user(email='ab@abv.bg', password='SummerTime123')
        article = self.create_article(
            title='Test',
            description='Test',
            url='https://sample.li/birds.jpeg',
            image='path/to/image.jpeg',
            user=article_user,
        )

        response = self.client.post(reverse('article likes', kwargs={
            'pk': article.id,
        }))

        self.assertEqual(302, response.status_code)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            article_id=article.id,
        ) \
            .exists()

        self.assertTrue(like_exists)

    def test_likeArticle__whenArticleAlreadyLiked_shouldDeleteTheLike(self):
        self.client.force_login(self.user)
        article_user = self.create_user(email='ab@abv.bg', password='SummerTime123')
        article = self.create_article(
            title='Test',
            description='Test',
            url='https://sample.li/birds.jpeg',
            image='path/to/image.jpeg',
            user=article_user,
        )

        response = self.client.post(reverse('article likes', kwargs={
            'pk': article.id,
        }))

        self.assertEqual(302, response.status_code)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            article_id=article.id,
        ) \
            .exists()

        self.assertTrue(like_exists)