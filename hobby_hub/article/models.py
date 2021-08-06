from django.db import models

# Create your models here.

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

    def __str__(self):
        return f'Article "{self.title}"'
