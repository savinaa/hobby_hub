from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

UserModel=get_user_model()

class Article(models.Model):
    title=models.CharField(
        max_length=120,
    )

    description=models.CharField(
        max_length=240,
    )

    url=models.URLField(

    )

    image=models.ImageField(
        upload_to='article'
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'Article "{self.title}"'

class Like(models.Model):
    article=models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )