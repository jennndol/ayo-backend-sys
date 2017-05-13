import os

import hashlib
import urllib

from django.contrib.auth.models import User
from django.db import models

from backend import settings


class Profile(models.Model):
    user = models.OneToOneField(User)
    bio = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'auth_profile'

    def __str__(self):
        return self.user.username

    def get_bio(self):
        return self.bio

    def get_picture(self):
        no_picture = settings.STATIC_ROOT + '/user.png'
        try:
            filename = settings.MEDIA_ROOT + '/profile_pictures/' + \
                       self.user.username + '.jpg'
            picture_url = settings.MEDIA_URL + 'profile_pictures/' + \
                          self.user.username + '.jpg'
            if os.path.isfile(filename):
                return picture_url

        except Exception:
            return no_picture

    def get_screen_name(self):
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()
            else:
                return self.user.username
        except:
            return self.user.username
