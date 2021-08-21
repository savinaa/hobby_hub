from django.urls import reverse

from tests.accounts.base.mixins import ArticleTestUtils, UserTestUtils
from tests.accounts.base.tests import HobbyHubTestCase


class ArticleDetailsTest(ArticleTestUtils, UserTestUtils, HobbyHubTestCase):

    def test_getArticleDetails_whenArticleExistsAndIsOwner_shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        article_user = self.create_user(email='ab@abv.bg', password='SummerTime123')
        article = self.create_article(
            title='Test',
            description='Test',
            url='https://sample.li/birds.jpeg',
            image='path/to/image.jpeg',
            user=article_user,
        )

        response = self.client.get(reverse('article details', kwargs={
            'pk': article.id,
        }))

        self.assertTrue(response.context['is_owner'])
        self.assertTrue(response.context['is_liked'])

    def test_getArticleDetails_whenArticleExistsAndIsNotOwnerAndNotLiked_shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        article_user = self.create_user(email='ab@abv.bg', password='SummerTime123')
        article = self.create_article(
            title='Test',
            description='Test',
            url='https://sample.li/birds.jpeg',
            image='path/to/image.jpeg',
            user=article_user,
        )

        response = self.client.get(reverse('article details', kwargs={
            'pk': article.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])

    def test_getArticleDetails_whenArticleExistsAndIsNotOwnerAndLiked_shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        article_user = self.create_user(email='ab@abv.bg', password='SummerTime123')
        article = self.create_article(
            title='Test',
            description='Test',
            url='https://sample.li/birds.jpeg',
            image='path/to/image.jpeg',
            user=article_user,
        )

        response = self.client.get(reverse('article details', kwargs={
            'pk': article.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])