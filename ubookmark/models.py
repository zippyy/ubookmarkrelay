from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class User(AbstractUser):
    pass

class BookmarkModel(models.Model):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    url = models.URLField(primary_key=True)
    comment = models.CharField(max_length=2048)
