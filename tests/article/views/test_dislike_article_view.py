from django.urls import reverse

from hobby_hub.article.models import Dislike
from tests.accounts.base.mixins import ArticleTestUtils, UserTestUtils
from tests.accounts.base.tests import HobbyHubTestCase


class dislikeArticleViewTests(ArticleTestUtils, UserTestUtils, HobbyHubTestCase):
    def test_dislikeArticle__whenArticleNotDisliked_shouldCreateDislike(self):
        self.client.force_login(self.user)
        article_user = self.create_user(email='ab@abv.bg', password='SummerTime123')
        article = self.create_article(
            title='Test',
            description='Test',
            url='https://sample.li/birds.jpeg',
            image='path/to/image.jpeg',
            user=article_user,
        )

        response = self.client.post(reverse('article dislikes', kwargs={
            'pk': article.id,
        }))

        self.assertEqual(302, response.status_code)

        dislike_exists = Dislike.objects.filter(
            user_id=self.user.id,
            article_id=article.id,
        ) \
            .exists()

        self.assertTrue(dislike_exists)

    def test_dislikeArticle__whenArticleAlreadyDisliked_shouldDeleteTheDislike(self):
        self.client.force_login(self.user)
        article_user = self.create_user(email='ab@abv.bg', password='SummerTime123')
        article = self.create_article(
            title='Test',
            description='Test',
            url='https://sample.li/birds.jpeg',
            image='path/to/image.jpeg',
            user=article_user,
        )

        response = self.client.post(reverse('article dislikes', kwargs={
            'pk': article.id,
        }))

        self.assertEqual(302, response.status_code)

        dislike_exists = Dislike.objects.filter(
            user_id=self.user.id,
            article_id=article.id,
        ) \
            .exists()

        self.assertTrue(dislike_exists)