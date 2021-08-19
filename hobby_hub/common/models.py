from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from hobby_hub.article.models import Article

UserModel = get_user_model()


class Comment(models.Model):
    text = models.TextField()
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )