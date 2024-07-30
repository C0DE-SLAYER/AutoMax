from django.db import models
from django.contrib.auth.models import User

from localflavor.in_.models import INStateField

from .util import user_upload_dir

class Location(models.Model):
    address_1 = models.CharField(max_length=120)
    address_2 = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=50)
    state = INStateField(default='MH')
    zip_code = models.IntegerField(default=400001)

    def __str__(self):
        return f"location: {self.id}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_upload_dir, null=True)
    bio = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
