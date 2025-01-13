from django.contrib.auth.models import AbstractUser
from django.db import models
from common.models import TimestampModel

class User(AbstractUser, TimestampModel):
    nickname    = models.CharField(max_length=20)
    profile_img = models.ImageField(blank=True, upload_to='profile_imgs/')
    bio         = models.TextField(blank=True)