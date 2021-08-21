import random
from os.path import join

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse

from hobby_hub.article.models import Article
from hobby_hub.hobby_hub_auth.models import Profile
from tests.accounts.base.tests import HobbyHubTestCase


class ProfileDetailsTest(HobbyHubTestCase):
    def test_getDetails_signedInUserWithoutArticles_getsDetailsWithNoArticles(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertListEmpty(list(response.context['articles']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)

    def test_getDetails_signedInUserWithArticles_getsDetailsWithArticles(self):
        article = Article.objects.create(
            title='Test',
            description='Test',
            url='https://sample.li/birds.jpeg',
            image='path/to/image.jpeg',
            user=self.user,
        )

        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.id, response.context['profile'].user_id)
        self.assertListEqual([article], list(response.context['articles']))

    def test_postDetails_signedInUserWithoutImage_shouldChangeImage(self):
        path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'test_image.jpeg')

        file_name = f'test_image.jpeg'
        file = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
            content_type='image/jpeg')

        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            'profile_image': file,
        })

        self.assertEqual(302, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)
        self.assertTrue(str(profile.profile_image).endswith(file_name))

    def test_postDetails_signedInUserWithImage_shouldChangeImage(self):
        path_to_image = 'path/to/image.jpeg'
        profile = Profile.objects.get(pk=self.user.id)
        profile.profile_image = path_to_image + 'old'
        profile.save()

        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            'profile_image': path_to_image,
        })

        self.assertEqual(200, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)