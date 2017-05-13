from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User)
    bio = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'auth_profile'

    def __str__(self):
        return self.user.username

    def get_bio(self):
        return self.bio