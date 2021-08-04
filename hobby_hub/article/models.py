from django.db import models

# Create your models here.

class Articles(models.Model):
    title=models.CharField(
        max_length=120,
    )

    description=models.CharField(
        max_length=240,
    )

    url=models.URLField(

    )

    image=models.ImageField(

    )
