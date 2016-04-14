from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

# from django.contrib.auth.models import User

'''
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    desc = models.TextField(blank=True, null=True)
'''


class User(AbstractUser):
    desc = models.TextField()

    # class Meta:
    #     model = User
    #     fields = ("username",)


# Create your models here.
class News(models.Model):
    list_field = ['id', 'news_thread', 'news_title', 'news_url', 'news_time', 'news_from', 'from_url', 'news_body']
    news_thread = models.TextField(blank=True, null=True)
    news_title = models.TextField(blank=True, null=True)
    news_url = models.TextField(blank=True, null=True)
    news_time = models.TextField(blank=True, null=True)
    news_from = models.TextField(blank=True, null=True)
    from_url = models.TextField(blank=True, null=True)
    news_body = models.TextField(blank=True, null=True)
    dele = models.BooleanField(default=0)

    def __str__(self):
        return models.Model.__str__(self)

    class Meta:
        db_table = 'news'
