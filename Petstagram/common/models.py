from django.contrib.auth.models import User
from django.db import models

from Petstagram.photos.models import Photo


class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True,)
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE,)


class Like(models.Model):
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE,)
