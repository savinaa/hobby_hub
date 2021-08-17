from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
# from hobby_hub.hobby_hub_auth.managers import HobbyHubUserManager
#
#
from hobby_hub.hobby_hub_auth.managers import HobbyHubUserManager


class HobbyHubUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    USERNAME_FIELD = 'email'

    objects = HobbyHubUserManager()


class Profile(models.Model):
    profile_picture = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    user = models.OneToOneField(
        HobbyHubUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
