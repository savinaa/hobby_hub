from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

class HobbyHubUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(
        unique=True,
    )
    profile_picture = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(auto_now_add=True, )

    USERNAME_FIELD='email'

    #user = models.OneToOneField(
    #    UserModel,
    #    on_delete=models.CASCADE,
    #    primary_key=True,
    #)
#
    #objects = AccountsUserManager()
